class Solution:
    def missingNumber(self, nums):
        missingNumber = len(nums)
        for i, num in enumerate(nums):
            missingNumber ^= i ^ num
        return missingNumber
