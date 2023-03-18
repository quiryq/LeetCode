# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        qur1 = []
        qur2 = []
        for i in range(len(s)):
            qur1.append(s.index(s[i]))
            qur2.append(t.index(t[i]))
        return qur1 == qur2