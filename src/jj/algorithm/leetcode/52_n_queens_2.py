# source: https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        res = 0
        
        def backtrack(r):
            if r == n:
                
                nonlocal res # 지역변수가 아님을 선언. 함수 바로 한 단계 바깥쪽에 위치한 변수와 바인딩 할 수 있다.
                
                res += 1
                
                return
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                    
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                
                backtrack(r + 1)
                
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                
        backtrack(0)
            
        return res