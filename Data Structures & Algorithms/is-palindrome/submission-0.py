class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())

        print(s)

        for i in range(int(len(s)/2)):
            if s[i] != s[len(s) - 1 -i]:
                return False

        return True
        