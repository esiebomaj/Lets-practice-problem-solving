class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # The required combination is a combination of TRANSPOSE and REFLECTION
        rows = len(matrix)
        cols = len(matrix[0])
        
        # TRANSPOSE
        for r in range(rows):
            for c in range(r+1):
                matrix[r][c], matrix[c][r] = matrix[c][r],  matrix[r][c]
                
        # REFLECTION
        for r in range(rows):
            for c in range(cols//2):
                matrix[r][c], matrix[r][-(c+1)] = matrix[r][-(c+1)], matrix[r][c]
                
        # print(matrix)
        
            