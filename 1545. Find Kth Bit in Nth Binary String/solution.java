class Solution {
    String reverse(String r) {
        char[] chars = new char[r.length()];

        int len = r.length() - 1;
        for (int j = 0; j < r.length(); j++)
            chars[len - j] = r.charAt(j);

        int i = 0;
        while (i < r.length()) {
            if (chars[i] == '0')
                chars[i] = '1';
            else
                chars[i] = '0';
            i++;
        }

        return String.valueOf(chars);
    }

    public char findKthBit(int n, int k) {

        String bit = "0";
        for (int i = 1; i < n; i++)
            bit = bit + "1" + reverse(bit);

        return bit.charAt(k - 1);
    }
}