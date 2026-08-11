# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # count freqs
#         # reverse sort by frequencies
#         # keep going until k met 
#         # and put in a list
#         # return list 

#         freqs = {}

#         for i in nums:
#             if i in freqs:
#                 freqs[i] += 1
#             else: 
#                 freqs[i] = 1
        
#         reverseSortedFreqs = dict(sorted(freqs.items(), key=lambda item : item[1], reverse=True))

#         sol = []
#         for key in reverseSortedFreqs.keys():
#             sol.append(key)
#             if len(sol) == k:
#                 break

#         return sol


from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies in O(n)
        freqs = Counter(nums)
        
        # Get top k elements in O(n log k) or O(n) depending on implementation
        # Returns a list of tuples: [(element, count), ...]
        top_k = freqs.most_common(k)
        
        # Extract just the elements
        return [item[0] for item in top_k]           