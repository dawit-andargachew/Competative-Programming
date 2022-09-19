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

        return new String(chars);
    }

    public char findKthBit(int n, int k) {

        String bit = "0";
        int i = 1;
        while (i < n) {
            bit = bit + "1" + reverse(bit);
            i++;
        }
        
        return bit.charAt(k - 1);
    }
}