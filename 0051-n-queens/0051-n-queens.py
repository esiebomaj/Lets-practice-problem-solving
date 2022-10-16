class Solution:        
    def solveNQueens(self, n: int) -> List[List[str]]:
        validRes = []
        
        def buildBoard(cols):
            res = []
            for i in range(n):
                row = ["."]*n
                row[cols[i]] = "Q"
                res.append("".join(row))
                
            return res
            
        
        def dfs(cols, posDia, negDia, r):
            
            if r == n:
                print(cols)
                validRes.append(buildBoard(cols))
                return 
                
            
            for c in range(n):
                if c not in cols and c+r not in negDia and c-r not in posDia:
                    cols.append(c)
                    posDia.add(c-r)
                    negDia.add(c+r)
                    
                    dfs(cols, posDia, negDia, r+1)
                    
                    cols.pop()
                    posDia.remove(c-r)
                    negDia.remove(c+r)
                    
        
        
        dfs([], set(), set(),  0)
        return validRes
            
        
        