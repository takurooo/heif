package box.boxes;
import box.FourCC;
import box.IBox;
import io.BinaryReader;

public class Box implements IBox{
    private int startPosition = 0;
    private int size = 0;
    private long largeSize = 0;
    private int type = 0;
    private int[] userType = new int[16];

    @Override
    public void parse(BinaryReader binaryReader) {
        this.startPosition = binaryReader.tell();
        this.size = binaryReader.read32();
        this.type = binaryReader.read32();
        if (this.size == 1) {
            this.largeSize = binaryReader.read64();
        }
        if (this.type == FourCC.UUID) {
            for (int i = 0; i < 16; i++) {
                this.userType[i] = binaryReader.read8();
            }
        }
    }

    @Override
    public long getSize() {
        if (this.largeSize == 0) {
            return (long) this.size;
        }
        return this.largeSize;
    }

    @Override
    public int getType() {
        return this.type;
    }

    public int getPosition() {
        return this.startPosition;
    }

    public void toBoxEnd(BinaryReader binaryReader) {
        long position = (long) this.getPosition() + this.getSize();
        binaryReader.seek(position, 0);
    }

}
