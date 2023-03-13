class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        two = []
        
        left, right = 0, len(numbers) - 1
        
        while left  < right:
            sum_ = numbers[left] + numbers[right]
            
            if sum_ == target:
                two.append(left + 1)
                two.append(right + 1)
                break
                
            elif sum_ > target:
                right -= 1
            else:
                left += 1
        
        return two
        