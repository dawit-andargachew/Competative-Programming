class Solution {
    // reverse and invert the given binary string
    String reverse(String r) {
        char[] chars = new char[r.length()];

        int len = r.length() - 1;
        for (int j = 0; j < r.length(); j++) // reverse
            chars[len - j] = r.charAt(j);

        int i = 0;
        while (i < r.length()) { // invert
            if (chars[i] == '0')
                chars[i] = '1';
            else
                chars[i] = '0';
            i++;
        }

        return String.valueOf(chars);
    }

    // main method
    public char findKthBit(int n, int k) {

        String bit = "0";
        for (int i = 1; i < n; i++)
            bit = bit + "1" + reverse(bit);

        return bit.charAt(k - 1);
    }
}