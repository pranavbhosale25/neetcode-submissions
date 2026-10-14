from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use 2 queues
        # start with 1st queue
        # push root
        # pop it and push its children in other queue
        # pop from 2nd q and push into 1st 
        # continue alternating until both qs empty 

        if not root:
            return []

        stack1, stack2 = deque(), deque()
        
        stack1.append(root)
        results = []

        # level 2 3
        # s1 4 5 6 7 
        # s2  
        # results [1] [2,3] 
        while stack1 or stack2:
            level = []
            while stack1:
                node = stack1.popleft()
                level.append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            # print(level)
            results.append(level)
            stack1,stack2 = stack2, stack1
        
        return results




        