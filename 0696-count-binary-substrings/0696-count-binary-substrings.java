class Solution {
  public int countBinarySubstrings(String s) {
    int count = 0;
    int i = 1;// we start at index 1
    int current_Len = 1;// so the start becomes 1 since we are starting from index 1
    int prev_c = 0;
      
      /// [1100], [11100], [001111],[1111100] => has two substring becase the minimum contigious length is 2, [0011]  and [10]
      // having length 2 for example also includes length 1 sub-strings
      // similarly, when s[i] != s[i+1] take the minimum as a substing
      // link - https://www.youtube.com/watch?v=MGPHPadxhtQ&t=249s
    while (i < s.length()) {
      if (s.charAt(i) == s.charAt(i - 1))// current and previous are the same, so increase current length
        current_Len++;
      else {/// if ther are not
        count += Math.min(prev_c, current_Len);
        prev_c = current_Len;
        current_Len = 1;
      }
      i++;
    }

    count += Math.min(prev_c, current_Len);
    return count;
  }
}