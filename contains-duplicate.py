class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset: 
                return True
            hashset.add(n)
        return False

def main():
    solution = Solution()
    test_nums = [1, 2, 3, 4, 1]
    print("Contains duplicates:", solution.containsDuplicate(test_nums))

if __name__ == "__main__":
    main()
