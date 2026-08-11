class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ''
        for s in strs:
            encoding += str(len(s)) + "✨" + s
        print(encoding)
        return encoding

    def decode(self, s: str) -> List[str]:

        # determine the num
        # slice the string
        # set start and current to next positions 
        # continue 

        start = 0 
        current = 1

        decoding = []
        while start < len(s) and current < len(s):
            # current += 1

            if s[current] == '✨':
                num = int(s[start:current])
                # 3#abc1000#xyz...
                decoding.append(s[current+1:current+1+num])
                start = current+1+num
                current = start + 1
            else: 
                current += 1

        return decoding

