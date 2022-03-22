class Solution {
    public String sortSentence(String s) {
         String[] sliced = s.split(" ");
        String[] sentence = new String[sliced.length];

        String complete_sentence = "";// holds the final sentence

        for (int i = 0; i < sliced.length; i++) {
            for (int j = 0; j < sliced.length; j++) {
                if (sliced[j].contains(Integer.toString(i + 1)))
                    sentence[i] = sliced[j].replace(Integer.toString(i + 1), ((i + 1 == sliced.length)) ? "" : " ");
            }
        }

        for (int i = 0; i < sliced.length; i++)
            complete_sentence += sentence[i];
        return complete_sentence;
    }
}