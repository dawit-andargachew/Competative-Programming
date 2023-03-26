class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        l, r = 0, len(letters) - 1
        while l <=r :
            mid = (l + r)//2

            if letters[mid] == target:
                
                # if the next charcter is the same iterate till the end
                while mid < len(letters) and letters[mid] == target:
                    mid += 1
                
                # check if it has next greater element
                if mid < len(letters):
                    return letters[mid]
                else:
                    return letters[0]

            elif letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        #if the last element is grater than target there exist a greater element to it and left points to the greater element
        if letters[-1] > target:
            return letters[l]
        else:
            return letters[0]