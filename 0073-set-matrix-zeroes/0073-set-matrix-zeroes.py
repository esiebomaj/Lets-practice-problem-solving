class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        firstRow = False
        firstCol = False
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
                    if r == 0:
                        firstRow = True
                    if c == 0:
                        firstCol = True
                        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if firstRow:
            for c in range(cols):
                matrix[0][c] = 0
                
        if firstCol:
            for r in range(rows):
                matrix[r][0] = 0
                
        
        
#         zeroRows = set()
#         zeroCols = set()
        
#         for r in range(rows):
#             for c in range(cols):
#                 if matrix[r][c] == 0:
#                     zeroCols.add(c)
#                     zeroRows.add(r)
                    
#         for r in range(rows):
#             for c in range(cols):
#                 if r in zeroRows or c in zeroCols:
#                     matrix[r][c] = 0
                    
        
        