class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        r1, r2 = 0, len(matrix)-1
        c1, c2 = 0, len(matrix[0])-1
        
        while r1 <= r2 and c1 <= c2:
            # print(r1, r2, c1, c2)
            for c in range(c1, c2+1):
                res.append(matrix[r1][c])
            r1+=1
            
            if r1 > r2 or c1 > c2:
                break
            
            # print(res)
            
            for r in range(r1, r2+1):
                res.append(matrix[r][c2])
            c2 -= 1
            
            if r1 > r2 or c1 > c2:
                break
            
            for c in range(c2, c1-1, -1):
                res.append(matrix[r2][c])
            r2 -= 1
            
            if r1 > r2 or c1 > c2:
                break
            
            for r in range(r2, r1-1, -1):
                res.append(matrix[r][c1])
            c1 += 1
            
                    
        # print(res)
        return res
            