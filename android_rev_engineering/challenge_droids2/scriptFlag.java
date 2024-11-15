// flag = picoCTF{what.is.your.favourite.colour}


public class scriptFlag {

    public static String getFlag() {
        String[] witches = {"weatherwax", "ogg", "garlick", "nitt", "aching", "dismass"};
        int second = 3 - 3;
        int third = (3 / 3) + second;
        int fourth = (third + third) - second;
        int fifth = 3 + fourth;
        int sixth = (fifth + second) - third;
        String password = "".concat(witches[fifth]).concat(".").concat(witches[third]).concat(".").concat(witches[second]).concat(".").concat(witches[sixth]).concat(".").concat(witches[3]).concat(".").concat(witches[fourth]);
        System.out.print(password);
        return null;
    }

    public static void main(String[] args) {
        getFlag();
    }
}
