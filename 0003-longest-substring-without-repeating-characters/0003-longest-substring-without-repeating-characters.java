class Solution {
    public int lengthOfLongestSubstring(String s) {

        int len = 0;
        for(int i = 0; i < s.length(); i++){
            List<Character> sub = new ArrayList();
            int j = i;
            while( j < s.length()){
                if(sub.contains(s.charAt(j)))
                    break;
                sub.add(s.charAt(j));
                j++;
            }

            len = Math.max(len,sub.size());
           }

        return len;
    }
}