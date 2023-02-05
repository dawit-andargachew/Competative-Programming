// class Solution {
//     public String decodeAtIndex(String s, int k) {
        
//         String decode = "";
//         for(char c : s.toCharArray()){
//             if( ! Character.isDigit(c))
//                 decode += c.toString();
//             else{
//                 int repeat = c - '0' - 1;
//                 String temp = decode;
//                 while( repeat > 0 && decode.length() < k){
//                     decode += temp;
//                     repeat--;
//                 }
//             }
//         }
        
        
//         return decode.charAt(k).toString();
//     }
// }
class Solution {
    public String decodeAtIndex(String S, int K) {
        for (int len = 0, i = 0; i < S.length(); i++) {
            if (Character.isDigit(S.charAt(i))) {
                int num = S.charAt(i) - '0', count = 0;
                for (; count < num - 1 && K > len; count++) {
                    K -= len;
                }
                if (count != num - 1) {
                    return decodeAtIndex(S, K);
                } else {
                    len *= num;
                }
            } else {
                len++;
                K--;
                if (K == 0) {
                    return String.valueOf(S.charAt(i));
                }
            }
        }
        return "";
    }
}