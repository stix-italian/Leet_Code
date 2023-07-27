class Solution:
    def isPalindrome(s: str) -> bool:
        import re
        # print(s)
        # s = s.lower()#.replace(' ','')
        print(s)
        s = re.sub(r'[^a-z0-9]+','',s.lower())
        # had just r'\W+' but it includes _ as a capture character.
        print(s)
        if s == s[::-1]:
            return True
        else:
            return False
    
    print(isPalindrome('ab_a'))