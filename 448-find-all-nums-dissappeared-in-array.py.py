class Solution:
    def findDisappearedNumbers(self, nums):

        # Create hash to store numbers
        number_hash = {}

        # Add all numbers to hash
        for num in nums:
            number_hash[num] = 1

        missing_numbers = []

        # Check if each number is in hash
        for i in range(1, len(nums) + 1):
            # If not in hash, add to missing numbers
            if i not in number_hash:
                missing_numbers.append(i)

        # Return missing numbers
        return missing_numbers

def main():
    solution = Solution()
    test_nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print("Disappeared numbers:", solution.findDisappearedNumbers(test_nums))

if __name__ == "__main__":
    main()
