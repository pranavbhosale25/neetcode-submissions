class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ignore non-alphanumeric
        # case insensitive

        s = s.lower()
        cleanS = ''.join(filter(str.isalnum, s))

        if len(cleanS) == 1:
            return True

        l = 0
        r = len(cleanS)-1

        while(l<r):
            if cleanS[l] != cleanS[r]:
                return False
            l += 1
            r -= 1

        return True

        