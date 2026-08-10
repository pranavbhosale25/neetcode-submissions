class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # dict - key encoding and value string

        # encode a string
        # if encoding exists - append
        # else add encoding and the new list 

        # iterate over the dict values and append into a list 
        # return the list of lists

        dictionary = {}

        for s in strs:
            # print(s)
            encoding = self.encode(s)
            if encoding in dictionary:
                dictionary[encoding].append(s)
            else:
                dictionary[encoding] = [s]

        sol = []
        for anagramList in dictionary.values():
            sol.append(anagramList)

        return sol
    
    def encode(self,s : str) -> str:
        return ''.join(sorted(s))


