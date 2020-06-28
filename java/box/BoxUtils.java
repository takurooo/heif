package box;

import box.boxes.Box;
import io.BinaryReader;

public class BoxUtils {

    public static Box readBox(BinaryReader binaryReader) {
        Box box = new Box();
        box.parse(binaryReader);
        binaryReader.seek(box.getPosition(), 0);
        return box;
    }

    public static void printBox(Box box) {
        System.out.printf("[%s] pos:0x%08x size:0x%08x%n",
                FourCC.toString(box.getType()),
                box.getPosition(),
                box.getSize());
    }

}
