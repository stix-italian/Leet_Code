def reverse(x):
  return x[::-1]

s = "babab"

# if reverse(s) == s:
#     print("yup")
# else: 
#    for x in range(0,len(s)):
#       if s[x] in s[x+1:]:
        #  then find farthest right position of x in s[x+1]
        # reverse s[x+1] and check if palindrome
          
def longestPal(s):
    def expand(l, r):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                return s[l+1:r]

    result = ""
    for i in range(len(s)):
        sub1 = expand(i, i)
        if len(sub1) > len(result):
            result = sub1
        sub2 = expand(i, i+1)
        if len(sub2) > len(result):
            result = sub2
    return result

longestPal('racecar')