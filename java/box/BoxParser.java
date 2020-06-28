package box;

import box.boxes.Box;
import box.boxes.MetaBox;
import io.BinaryReader;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.file.Files;
import java.nio.file.Paths;

public class BoxParser {
    BinaryReader binaryReader;
    MetaBox metaBox;

    public BoxParser() {

    }

    public void parseBoxes(String fileName) throws IOException {
        System.out.println(fileName);
        byte[] content = Files.readAllBytes(Paths.get(fileName));
        this.binaryReader = new BinaryReader(ByteBuffer.wrap(content));

        while(!this.binaryReader.isEnd()) {
            Box box = BoxUtils.readBox((this.binaryReader));
            long boxSize = box.getSize();
            int boxType = box.getType();

            BoxUtils.printBox(box);

            if(boxType == FourCC.FTYP) {
                this.binaryReader.seek(boxSize,1);
            }
            else if(boxType == FourCC.MOOV) {
                this.binaryReader.seek(boxSize,1);
            }
            else if(boxType == FourCC.META) {
                this.metaBox = new MetaBox();
                this.metaBox.parse(this.binaryReader);
            }
            else if(boxType == FourCC.MDAT) {
                this.binaryReader.seek(boxSize,1);
            }
            else if(boxType == FourCC.FREE) {
                this.binaryReader.seek(boxSize,1);
            }
            else {
                this.binaryReader.seek(boxSize,1);
            }
        }

    }
}
