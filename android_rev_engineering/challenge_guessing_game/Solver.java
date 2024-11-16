import java.util.Random;

public class Solver {
    private static final char[] HEX_CHARS = "0123456789abcdef".toCharArray();
    private byte[] encryptedFlag;
    private final String flag;
    private int index;
    private Random rand;
    private int[] sequence;

    /*
     * JADX WARN: Type inference failed for: r0v4, types:
     * [it.m0lecon.workshop.guessinggame.MainActivity$1]
     */
    public Solver() {
        Random random = new Random();
        this.rand = random;
        this.sequence = new int[] { random.nextInt(), this.rand.nextInt(), this.rand.nextInt(), this.rand.nextInt() };
        this.index = 0;
        this.flag = new Object() { // from class: it.m0lecon.workshop.guessinggame.MainActivity.1
            int t;

            public String toString() {
                this.t = 1905553571;
                this.t = -1012727321;
                this.t = 798602950;
                this.t = 129258562;
                this.t = -405136503;
                this.t = 768131176;
                this.t = -1137058184;
                this.t = 151775514;
                this.t = -1322004596;
                this.t = -2405354;
                this.t = 424107935;
                this.t = 1606351404;
                this.t = -1327256133;
                this.t = 880707601;
                this.t = 865830133;
                this.t = -311163277;
                this.t = 2093900761;
                this.t = 1555702477;
                this.t = 1080538790;
                this.t = 2065274444;
                this.t = -600268035;
                this.t = 736941457;
                this.t = 409405908;
                this.t = -1171481881;
                this.t = -946971024;
                this.t = 1620772542;
                this.t = 745582738;
                this.t = -665392404;
                this.t = 1631162897;
                this.t = -1716641030;
                this.t = -1154840086;
                this.t = 865891027;
                this.t = -605342860;
                byte[] buf = { (byte) (1905553571 >>> 8), (byte) ((-1012727321) >>> 19), (byte) (798602950 >>> 7),
                        (byte) (129258562 >>> 20), (byte) ((-405136503) >>> 6), (byte) (768131176 >>> 10),
                        (byte) ((-1137058184) >>> 10), (byte) (151775514 >>> 13), (byte) ((-1322004596) >>> 11),
                        (byte) ((-2405354) >>> 6), (byte) (424107935 >>> 12), (byte) (1606351404 >>> 24),
                        (byte) ((-1327256133) >>> 5), (byte) (880707601 >>> 24), (byte) (865830133 >>> 19),
                        (byte) ((-311163277) >>> 16), (byte) (2093900761 >>> 18), (byte) (1555702477 >>> 22),
                        (byte) (1080538790 >>> 17), (byte) (2065274444 >>> 4), (byte) ((-600268035) >>> 3),
                        (byte) (736941457 >>> 9), (byte) (409405908 >>> 22), (byte) ((-1171481881) >>> 13),
                        (byte) ((-946971024) >>> 20), (byte) (1620772542 >>> 1), (byte) (745582738 >>> 7),
                        (byte) ((-665392404) >>> 12), (byte) (1631162897 >>> 10), (byte) ((-1716641030) >>> 3),
                        (byte) ((-1154840086) >>> 2), (byte) (865891027 >>> 24), (byte) ((-605342860) >>> 19) };
                return new String(buf);
            }
        }.toString();

        System.out.println(flag);
    }

    public static void main(String[] args) {
        new Solver();
        // ptm{n0w_y0u_m4st3r3d_jadx_and_z3}
    }
}