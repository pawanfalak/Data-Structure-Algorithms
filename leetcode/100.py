# Definition for a binary tree node.
from typing import Optional 
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS with stack
        stack = [(p, q)]
        while len(stack):
            p, q = stack.pop()
            if not p and not q:
                continue
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            stack.append((p.right, q.right))
            stack.append((p.left, q.left))
        return True
        
        # BFS with queue
        # queue = deque([(p,q)])
        # while len(queue):
        #     p, q = queue.popleft()
        #     if not p and not q:
        #         continue
        #     elif not p or not q:
        #         return False
        #     elif p.val != q.val:
        #         return False
        #     queue.append((p.left, q.left))
        #     queue.append((p.right, q.right))
        # return True
        
        # Recursion
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)