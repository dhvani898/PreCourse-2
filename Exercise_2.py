# Python program for implementation of Quicksort Sort 
# Time Complexity: O(N2)
 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        lower = []
        bigger = []
        
        if (length <=1):
            return nums
        else:
            pivot = nums.pop()
            for i in range(length - 1):
                if(pivot<nums[i]):
                    bigger.append(nums[i])
                else:
                    lower.append(nums[i])
        return self.sortArray(lower) + [pivot] + self.sortArray(bigger)
 
