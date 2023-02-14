import java.util.Stack;

class Solution {
    public int compress(char[] chars) {
        if (chars.length == 1)
            return 1;
        Stack<Character> key = new Stack();
        Stack<Integer> value = new Stack();

        // hash map does't work for this problems becase Duplicate keys are not allowed
        // like a,a,a,b,b,a => a3b2a

        // let's compress the string with two stacks, one for key another for values
        // step 1, keys = a,b,a and values = 3,2,1
        // so if the key.peek() == char, increase frequency by one
        // else store the new character with frequency of 1
        // step 2, modify the input array
        /// if frequency == 1 > just store key
        // else if frequency > 1 && < 9 => store key and value
        // else if frequency > 10 => store the reminder to another stack, and put on
        // origin array

        // step 1
        for (char c : chars) {
            if (!key.isEmpty() && key.peek() == c) {
                int val = value.pop();
                value.push(val + 1);
                // int size = value.size();
                // value.set( size - 1, value.get( size - 1) + 1);
            } else {
                key.push(c);
                value.push(1);
            }
        }

        // step 2, modify the input array and count new length of array
        int new_length = 0;
        int index = 0;
        for (int i = 0; i < key.size(); i++) {
            chars[index++] = key.get(i);
            new_length++;

            int frequency = value.get(i);
            if (frequency > 1 && frequency < 10) {
                chars[index++] = (char) ('0' + frequency);
                new_length++;
            } else if (frequency >= 10) {

                Stack<Integer> temp = new Stack();
                while (frequency != 0) {
                    int remainder = frequency % 10;
                    temp.push(remainder);
                    new_length++;

                    frequency /= 10;
                }

                while (!temp.isEmpty())
                    chars[index++] = (char) ('0' + temp.pop());
            }
        }

        return new_length;
    }
}