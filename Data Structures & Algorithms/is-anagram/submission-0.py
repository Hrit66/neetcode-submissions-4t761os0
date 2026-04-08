class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hasList=[0]*26
        for ch in s:
            ascii = ord(ch)
            index = ascii - 97
            hasList[index]+=1
        for ch in t:
            ascii = ord(ch)
            index = ascii - 97
            hasList[index]-=1
            if hasList[index] < 0:
               return False
        return True
