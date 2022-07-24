# Leetcode
# word search, medium
# https://leetcode.com/problems/word-search/

class Solution(object):    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, c, visited):
            result = 0
            if (i, j) in visited:
                return False
            if i < 0 or j < 0 or i > len(board)-1 or j > len(board[0])-1:
                return False
            visited.append((i, j))

            if word[c] == board[i][j]:
                if c == len(word) - 1:
                    return True
                result += dfs(i+1, j, c+1, visited)
                result += dfs(i-1, j, c+1, visited)
                result += dfs(i, j+1, c+1, visited)
                result += dfs(i, j-1, c+1, visited)

            visited.remove((i, j))

            return result
        
        answer = 0
        for i, line in enumerate(board):
            for j, x in enumerate(line):
                if x == word[0]:
                    visited = list()
                    answer += dfs(i, j, 0, visited)
                    if answer:
                        return answer
                    
        return answer