package box;

public class FourCC {
    public static final int FTYP = toInt("ftyp");
    public static final int UUID = toInt("uuid");
    public static final int FREE = toInt("free");
    public static final int MOOV = toInt("moov");
    public static final int META = toInt("meta");
    public static final int MDAT = toInt("mdat");
    public static final int HDLR = toInt("hdlr");
    public static final int PITM = toInt("PITM");
    public static final int IINF = toInt("IINF");
    public static final int IPRP = toInt("IPRP");
    public static final int IREF = toInt("IREF");
    public static final int ILOC = toInt("iloc");

    public static int toInt(String fourcc) {
        char[] arr = fourcc.toCharArray();
        return arr[0] << 24 | arr[1] << 16 | arr[2] << 8 | arr[3];
    }

    public static String toString(int fourcc) {
        char[] arr = new char[4];
        arr[0] = (char)((fourcc >> 24) & 0xff);
        arr[1] = (char)((fourcc >> 16) & 0xff);
        arr[2] = (char)((fourcc >> 8) & 0xff);
        arr[3] = (char)(fourcc & 0xff);

        return String.valueOf(arr);
    }
}
