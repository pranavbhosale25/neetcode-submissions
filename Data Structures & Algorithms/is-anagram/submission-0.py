class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alphabetCountsS = [0] * 26
        alphabetCountsT = [0] * 26

        for i in range(len(s)):
            alphabetCountsS[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            alphabetCountsT[ord(t[i]) - ord('a')] += 1

        for i in range(26): 
            if alphabetCountsS[i] != alphabetCountsT[i]:
                return False
        
        return True


        