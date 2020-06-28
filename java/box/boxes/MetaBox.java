package box.boxes;

import box.BoxUtils;
import box.FourCC;
import io.BinaryReader;

public class MetaBox extends FullBox {
    public void parse(BinaryReader binaryReader) {
        super.parse(binaryReader);

        Box box = BoxUtils.readBox((binaryReader));
        long boxSize = box.getSize();
        int boxType = box.getType();

        BoxUtils.printBox(box);

        if (boxType == FourCC.FTYP) {
            binaryReader.seek(boxSize, 1);
        } else if (boxType == FourCC.HDLR) {
            binaryReader.seek(boxSize, 1);
        } else if (boxType == FourCC.PITM) {
            binaryReader.seek(boxSize, 1);
        } else if (boxType == FourCC.ILOC) {
            binaryReader.seek(boxSize, 1);
        } else if (boxType == FourCC.IINF) {
            binaryReader.seek(boxSize, 1);
        } else if (boxType == FourCC.IPRP) {
            binaryReader.seek(boxSize, 1);
        } else {
            binaryReader.seek(boxSize, 1);
        }
    }
}
