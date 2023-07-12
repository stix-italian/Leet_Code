# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
def isValid(s: str) -> bool:
    if len(s) < 2:
        return False
    if not len(s) % 2 == 0:
        return False 
    check = []
    for x in range(0,len(s)):
        if s[x]=='(':
            open_paren = True
            check.append(open_paren)
        elif s[x]==')':
            open_paren = False
            check.append(open_paren)
            # if not s[x+1]==')':
            #     return False
        elif s[x]=='[':
            open_box = True
            check.append(open_box)
        elif s[x]==']':
            open_box = False
            # if not s[x+1]==']':
            #     return False
        elif s[x]=='{':
            open_brack = True
            check.append(open_brack)
        elif s[x]=='}':
            open_brack = False
            # if not s[x+1]=='}':
            #     return False
    for y in check:
        if y:
            return False
    return True

isValid('()')