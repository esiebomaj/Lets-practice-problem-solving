class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        zeroRows = set()
        zeroCols = set()
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeroCols.add(c)
                    zeroRows.add(r)
                    
        for r in range(rows):
            for c in range(cols):
                if r in zeroRows or c in zeroCols:
                    matrix[r][c] = 0
                    
        
        