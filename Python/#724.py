# 724. Find Pivot Index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            x = nums[i + 1 : len(nums)]
            b = nums[:i]
            right_sum = sum(x)
            left_sum = sum(b)            
            if left_sum == right_sum:
                return i
        return -1    