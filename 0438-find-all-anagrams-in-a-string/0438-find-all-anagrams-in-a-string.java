class Solution{
public List<Integer> findAnagrams(String s, String p) {
    // here is  a two pointer problem and we need to store the frequency of each characters in p
    // and lets use int array to store it [which has 26 characters]
    // 
    // the code works like this,
    //       it uses two pointers right and left and every time counter == 0 we add the left to the list
    //
    // case-1, hash[s.charAt(right++) - 'a'] -- >= 1
    //         there is increment operator, and if it has occurence on it
    //         map[xx] decreased, right++, and [count-- if it has occurence on string p]
    // case-2 when ever the difference beween left and right is p.length()
    //          map[xx] increased and left++, and [count++ if it has more than 1 occurence in p]


    List<Integer> list = new ArrayList<>();
    
    // if either of them are empty, just return empty list there is no anagram at all
    if (s.length() == 0 || p.length() == 0)
        return list;

    // store the frequency of each characters
    int[] hash = new int[26];
    for (char c : p.toCharArray()) 
        hash[c -'a']++;
    
    int left = 0, right = 0, count = p.length();
    while (right < s.length()) {
        
        //move right everytime, if the character exists in p's hash, decrease the count
        //current hash value >= 1 means the character is existing in p
        if (hash[s.charAt(right++) -'a']-- >= 1) 
            count--; 
        
        //when the count is down to 0, means we found the right anagram
        //then add window's left to result list
        if (count == 0) 
            list.add(left);
    
        //if we find the window's size equals to p, then we have to move left (narrow the window) to find the new match window
        //++ to reset the hash because we kicked out the left
        //only increase the count if the character is in p
        //the count >= 0 indicate it was original in the hash, cuz it won't go below 0
        if (right - left == p.length() && hash[s.charAt(left++) - 'a']++ >= 0)
            count++;
    }
    return list;
    }
}