# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for letter in range(len(t)):
            if i == len(s):
                return True
            if s[i] == t[letter]:
                i += 1
        return i == len(s)