class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1:
            return False

        stack = deque()

        # for open braces - push in 
        # for close braces- check if top matches
        # if not return false , 
        # if yes, pop and continue

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')' :
                if stack and stack[-1] != '(' or (not stack):
                    return False
                elif stack:
                    stack.pop()
            elif c == ']' :
                if stack and stack[-1] != '[' or (not stack):
                    return False
                elif stack:
                    stack.pop()
            elif c == '}' :
                if stack and stack[-1] != '{' or (not stack):
                    return False
                elif stack:
                    stack.pop()
                
        if stack:
            return False
        else:
            return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stack = deque()

        # for c in s: 
        #     if c == '(' or c == '[' or c == '{':
        #         stack.append(c)
        #     elif c == ')':
        #         if stack and stack[-1] == '(':
        #             stack.pop()
        #         else:
        #             return False
        #     elif c == ']':
        #         if stack and stack[-1] == '[':
        #             stack.pop()
        #         else:
        #             return False
        #     elif c == '}':
        #         if stack and stack[-1] == '{':
        #             stack.pop()
        #         else:
        #             return False

        # if stack:
        #     return False
        # return True
        