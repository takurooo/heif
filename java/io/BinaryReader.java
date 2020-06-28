package io;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;

public class BinaryReader {
    ByteBuffer byteBuffer;
    int maxSize;

    public BinaryReader(ByteBuffer byteBuffer) {
        this.byteBuffer = byteBuffer;
        this.byteBuffer.order(ByteOrder.BIG_ENDIAN);
        this.maxSize = this.byteBuffer.limit();
    }

    public BinaryReader createBinaryReader(int length) {
        byte[] b = new byte[length];
        this.byteBuffer.get(b, 0, length);
        ByteBuffer subByteBuffer = ByteBuffer.wrap(b);
        return new BinaryReader(subByteBuffer);
    }

    public byte read8() {
        return this.byteBuffer.get();
    }

    public short read16() {
        return this.byteBuffer.getShort();
    }

    public int read24() {
        byte[] x = new byte[3];
        int out24 = 0;
        x[0] = this.read8();
        x[1] = this.read8();
        x[2] = this.read8();

        if(this.byteBuffer.order() == ByteOrder.BIG_ENDIAN) {
            out24 = x[0] << 16 | x[1] << 8 | x[2];
        }
        else {
            out24 = x[2] << 16 | x[1] << 8 | x[0];
        }

        return out24;
    }

    public int read32() {
        return this.byteBuffer.getInt();
    }

    public long read64() {
        return this.byteBuffer.getLong();
    }

    public int numByteLeft() {
        return this.byteBuffer.remaining();
    }

    public boolean isEnd() {
        return this.numByteLeft() <= 0;
    }

    public int tell() {
        return this.byteBuffer.position();
    }

    public void seek(int position, int whence) {
        int newPotision = 0;

        switch (whence) {
            case 0: // from start
                newPotision = position;
                break;
            case 1: // from current
                newPotision = this.byteBuffer.position() + position;
                break;
            case 2: // from end
                newPotision = this.maxSize + position;
                break;
            default:
                assert false : "Invalid value:" + whence;
                break;
        }
        this.byteBuffer.position(newPotision);
    }

    public void seek(long position, int whence) {
        long seekSize = 0;

        switch (whence) {
            case 0: // from start
                seekSize = position;
                break;
            case 1: // from current
                seekSize = this.byteBuffer.position() + position;
                break;
            case 2: // from end
                seekSize = this.maxSize + position;
                break;
            default:
                assert false : "Invalid value:" + whence;
                break;
        }


        boolean isFirst = true;
        while (seekSize > 0) {
            int newPosition;
            int newWhence;

            if (seekSize > Integer.MAX_VALUE) {
                newPosition = Integer.MAX_VALUE;
            } else {
                newPosition = (int) seekSize;
            }

            if (isFirst) {
                newWhence = 0;
                isFirst = false;
            } else {
                newWhence = 1;
            }

            this.seek(newPosition, newWhence);

            seekSize -= newPosition;
        }
    }
}


