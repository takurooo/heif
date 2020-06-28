import box.BoxParser;

import java.io.IOException;

public class Main {

    public static void main(String args[]) throws IOException {

        if(args.length != 1) {
            System.out.println("erro invalid args");
            System.exit(1);
        }

        String inFileName = args[0];

        BoxParser boxParser = new BoxParser();
        boxParser.parseBoxes(inFileName);
    }
}
