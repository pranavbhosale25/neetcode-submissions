class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # how far ahead is the next biggest temp 
        if len(temperatures) == 0:
            return [0]

        # our stack stores indices, not elements
        # 30 38 30 36 35 40 28
        # 38 40 36 40 40 0 0 
        # stack 40 38
        # pop until bigger than me found - put index of that at current location
        # if empty put 0 
        # then insert current in stack 

        stack = []
        ans = [0] * len(temperatures)

        # start from back 
        for i in range(len(temperatures)-1,-1,-1):
            # stack not empty and top is less than me? keep popping 
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            # else ans[i] remains 0 

            stack.append(i)
        
        return ans
