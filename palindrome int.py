# Given an integer x, return true if x is a palindrome,
# and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



def isPalindrome(x: int) -> bool:
    x=str(x)
    y=x
    return y[::-1]==x
    # this is the fastest & least memory used overall
    # return str(x)==(str(x)[::-1]) - is very memory effecient but slow 85ms
    

print(isPalindrome(121))

print(isPalindrome(-121))

print(isPalindrome(10))


print(isPalindrome(1000000000001))
