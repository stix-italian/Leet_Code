class Solution:



    def buddyStrings(s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(set(s)) != len(set(goal)):
            return False
        
        # for x in range(0,len(s)):
        #     for y in range(1,len(s)):
        #         if x == y:
        #             pass
        #         elif s[x] == s[y]:
        #             return True
        # for x in range(0,len(s)):
        #     for y in range(0,len(goal)):
        #         if s[x] == goal[y] and x != y:
        #             return True
        
        def swap(s,i,j):
            s_list=list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            s = ''.join(s_list)
            return s

        temp = s[:]
        for x in range(0,len(s)):
            for y in range(1,len(s)):
                if s[x] == s[y] and x != y:
                    if swap(s,x,y) == goal:
                        return True
        for x in range(0,len(s)):
            for y in range(0,len(goal)):
                if s[x] == goal[y] and x != y:
                    if swap(s,x,y) == goal:
                        return True      
        
        return False

           
    print(buddyStrings('ab','ba'))