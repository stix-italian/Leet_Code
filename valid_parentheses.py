# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# getting mad at "([)]" because of order of operations. Can't close your parenthese in the middle of an operation. 
def isValid(s: str) -> bool:
    if len(s) < 2:
        return False
    if not len(s) % 2 == 0:
        return False 
    open_paren = True
    open_box = True
    open_brack = True
    for x in range(0,len(s)):
        if s[x]=='(':
            open_paren = False
        elif s[x]==')':
            open_paren = True
        elif s[x]=='[':
            open_box = False
        elif s[x]==']':
            open_box = True
        elif s[x]=='{':
            open_brack = False
        elif s[x]=='}':
            open_brack = True
    if not open_paren or not open_box or not open_brack:
        return False
    return True


isValid('()')
isValid("([)]")
isValid("{()}")


# Old Code

    # if len(s) < 2:
    #     return False
    # if not len(s) % 2 == 0:
    #     return False 
    # # check = []
    # open_paren = True
    # open_box = True
    # open_brack = True
    # for x in range(0,len(s)):
    #     if s[x]=='(':
    #         open_paren = False
    #         # check.append(open_paren)
    #     elif s[x]==')':
    #         open_paren = True
    #         # if not s[x+1]==')':
    #         #     return False
    #     elif s[x]=='[':
    #         open_box = False
    #         # check.append(open_box)
    #     elif s[x]==']':
    #         open_box = True
    #         # if not s[x+1]==']':
    #         #     return False
    #     elif s[x]=='{':
    #         open_brack = False
    #         # check.append(open_brack)
    #     elif s[x]=='}':
    #         open_brack = True
    #         # if not s[x+1]=='}':
    #         #     return False
    # # for y in check:
    # #     if y:
    # #         return False
    # if not open_paren or not open_box or not open_brack:
    #     return False
    # return True
