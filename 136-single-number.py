class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        missingNumber = 0
        for num in nums:
            missingNumber ^= num
        return missingNumber
