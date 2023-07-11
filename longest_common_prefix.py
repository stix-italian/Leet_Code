from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    overall = -1
    if len(strs) == 1:
            overall = len(strs[0])
    else:
        for x in range(0,len(strs)-1):
            longest = 0
            if strs[x] == strs[x+1]:
                longest= len(strs[x])
            else:
                shortest = len(strs[x])
                if len(strs[x+1]) < shortest:
                    shortest = len(strs[x+1])
                for y in range (0,shortest):
                    if strs[x][y] == strs[x+1][y]:
                        longest += 1
                    else:
                        break
            if longest < overall and overall > -1:
                    overall = longest
            elif overall == -1:
                overall = longest
    if overall == -1:
        overall = 0
    return strs[0][:overall]


print(longestCommonPrefix(['fl','flower','flower']))
print(longestCommonPrefix(['a']))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["reflower","flow","flight"]))

# Answer from Leet Code Submissions that I liked:
#  Key things that were done:
#  1 return the empty lists or lists of length 1 right at the start
#  2 sort your list. 
#  3 with a sorted list you only have to compare the shortest and longest word. Everything must be the same so the middle words don't matter!
    # a= strs
    # size = len(a)

    # # if size is 0, return empty string
    # if (size == 0):
    #     return ""

    # if (size == 1):
    #     return a[0]

    # # sort the array of strings
    # a.sort()

    # # find the minimum length from
    # # first and last string
    # end = min(len(a[0]), len(a[size - 1]))    could also do len(a[-1]) for the last element in a list

    # # find the common prefix between
    # # the first and last string
    # i = 0
    # while (i < end and
    #     a[0][i] == a[size - 1][i]):
    #     i += 1

    # pre = a[0][0: i]
    # return pre