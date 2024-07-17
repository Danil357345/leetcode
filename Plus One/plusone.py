class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        # Traverse the list from the end to the start
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If all the digits are 9, the result will be a leading 1 followed by n zeroes
        return [1] + [0] * n

# Test cases
solution = Solution()
print(solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(solution.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(solution.plusOne([9]))  # Output: [1, 0]
