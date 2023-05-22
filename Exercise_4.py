# Python program for implementation of MergeSort 
# https://leetcode.com/problems/sort-an-array/
# Time Complexity : O(NlogN)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if(len(nums)>1):
            left_arr = nums[:(len(nums)//2)]
            right_arr = nums[(len(nums)//2):]
            new_arr = [ ]
            left_arr = self.sortArray(left_arr)
            right_arr = self.sortArray(right_arr)
            i = 0
            j = 0
            k = 0
            while(i<len(left_arr) and j<len(right_arr)):
                if(left_arr[i]<right_arr[j]):
                    new_arr.append(left_arr[i])
                    i+=1
                else:
                    new_arr.append(right_arr[j])
                    j+=1
            while(i<len(left_arr)):
                new_arr.append(left_arr[i])
                i+=1
            while(j<len(right_arr)):
                new_arr.append(right_arr[j])
                j+=1
            return new_arr
        return nums





