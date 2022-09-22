# LeetCode Easy Problem
# using algorithm BFS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def __init__(self):
        self._visited_p = list()
        self._visited_q = list()
        self._queue_p = None
        self._queue_q = None
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self._queue_p = deque([p])
        self._queue_q = deque([q])
        
        while self._queue_p and self._queue_q:
            n_p = self._queue_p.popleft()
            n_q = self._queue_q.popleft()
            if n_p and n_p not in self._visited_p:
                self._visited_p.append(n_p.val)
                self._queue_p += set([n_p.left]) - set(self._visited_p)
                self._queue_p += set([n_p.right]) - set(self._visited_p)

            if n_q and n_q not in self._visited_q:
                self._visited_q.append(n_q.val)
                self._queue_q += set([n_q.left]) - set(self._visited_q)
                self._queue_q += set([n_q.right]) - set(self._visited_q)
            
            if self._visited_p != self._visited_q:
                return False
        
        return self._visited_p == self._visited_q