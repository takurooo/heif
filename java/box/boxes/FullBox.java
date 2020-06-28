package box.boxes;

import box.IFullBox;
import box.ParsableBox;
import io.BinaryReader;

public class FullBox extends Box implements IFullBox {
    private byte version;
    private int flags;

    public FullBox(){

    }

    @Override
    public void parse(BinaryReader binaryReader) {
        super.parse(binaryReader);
        this.version = binaryReader.read8();
        this.flags = binaryReader.read24();
    }

    @Override
    public byte getVersion() {
        return this.version;
    }

    @Override
    public int getFlags() {
        return this.flags;
    }
}
