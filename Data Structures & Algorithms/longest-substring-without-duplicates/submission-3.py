# Cleaner Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        left = 0
        longest = 0

        for right, c in enumerate(s):
            if c in charMap:
                left = max(left, charMap[c] + 1)

            charMap[c] = right
            longest = max(longest, right - left + 1)

        return longest

# My Solution
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # traverse the string
#         # maintain a dict of char and its latest index
#         # also maintain start index (left and right ptrs)
#         # at each char , if its present in the dict 
#         # and its index lies between left and right index 
#         # update left to that position + 1 
#         # also update that chars index in dict either way 

#         strLen = len(s)
#         if strLen == 0 or strLen == 1: 
#             return strLen

#         charMap = {}
#         left = 0
#         right = 1
        
#         solLen = 0
#         charMap[s[left]] = left

#         # longestSubstringLength 
#         lsl = 0 

#         while right < strLen:
#             if s[right] in charMap:
#                 if left <= charMap[s[right]]: # it's present in the current substring!
#                     # lsl = max(lsl, right-left)
#                     left = charMap[s[right]] + 1 # take to where you found right and 1 step ahead
#             lsl = max(lsl, right-left+1)    
#             charMap[s[right]] = right
#             right += 1

#         return lsl





