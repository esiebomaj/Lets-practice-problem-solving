class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[1 for i in range(n)] for j in range(m)]
        for r in range(1,m):
            for c in range(1,n):
                board[r][c] = board[r-1][c] + board[r][c-1]
        return board[-1][-1]
        