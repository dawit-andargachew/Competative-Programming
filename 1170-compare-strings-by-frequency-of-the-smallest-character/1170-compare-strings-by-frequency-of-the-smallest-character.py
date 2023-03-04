class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # what does lexicographically smallest character in a string mean?
        #      take s = "dccefg", 'c' is lexicographically smallest b/ce is appear fist in the alphabet
        #
        # The question is simply, to count the number of words in `words`, such that
        #        f(queries[i]) < f(W)
        # solution: sort f(words[i]) and apply binary search until the above condition meet
        
        # step-1 : And, `f(s)` is the frequency of the lexicographically smallest character, how to get this?
        #          sort the strig and find the frequency of zeroth index
        #          s = sorted("dccefg") gives "ccdefg" => s[0] => 'c' => is lexicographically smallest
        #     -> So the frequency of the lexicographically smallest character is => s.count(s[0])
        #          

        # step-2: To apply binary search, sort the frequency

        # step-3: 
        #   case-1: f(queries[i]) has no greater element in f(words)
        #           f(words) is sorted so f(queries[i]) >= f(words)[-1]  =>  has no greater element
        #           
        #   case-2: f(queries[i]) has greater element in f(words[i])
        #           apply binary search whenver we get greater element store the index

        count = []

        #Step-1: the frequency of the lexicographically smallest character in Words
        for i in range(len(words)):
            w = sorted(words[i])
            words[i] =w.count(w[0]) # stores the frequency of  lexicographically smallest char

        #step:2 sort to apply binary search
        words.sort() 

        # store  frequency of the lexicographically smallest for qeuries
        for i in range(len(queries)):
            q = sorted(queries[i])
            queries[i] =q.count(q[0])

        # step3: apply binary search for each queries
        for q in queries:

            low = 0
            high = len(words) - 1

            # case-1
            if q >= words[-1]:
                count.append(0)
            
            # case-2
            else:
                index = 0

                while low <= high:
                    mid = low + (high - low)//2

                    if q < words[mid]:
                        index = mid
                        high = mid - 1
                    else:
                        low = mid + 1

                count.append( len(words) - index )

        return count