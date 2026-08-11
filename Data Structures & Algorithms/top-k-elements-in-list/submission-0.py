class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count freqs
        # reverse sort by frequencies
        # keep going until k met 
        # and put in a list
        # return list 

        freqs = {}

        for i in nums:
            if i in freqs:
                freqs[i] += 1
            else: 
                freqs[i] = 1
        
        reverseSortedFreqs = dict(sorted(freqs.items(), key=lambda item : item[1], reverse=True))


        sol = []
        for key in reverseSortedFreqs.keys():
            if len(sol) == k:
                break
            sol.append(key)

        return sol


        