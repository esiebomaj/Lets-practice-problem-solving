class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # go through the entire board
        # if we see a zero that has not been seen before 
        # we do bfs on it 
        # while doing the bfs we ensure that its not bounded by any edge
        
        # determine where to capture
        
        seen = set()
        
        rows = len(board)
        cols = len(board[0])
        
        def bfs(r, c):
            
            q = [(r,c)]
            to_be_captured = set([(r,c)])
            capture = True
            
            while q:
                
                curr = q.pop()
                seen.add(curr)
                
                for dy, dx in [[1,0], [-1,0], [0,1], [0,-1]]:
                    i,j = curr[0]+dy, curr[1]+dx
                    
                    if i < 0 or i >= rows or j < 0 or j >= cols:
                        # if out of bounds
                        capture = False
                    else:
                        # not out of bounds
                        if board[i][j] == "O" and (i,j) not in seen:
                            to_be_captured.add((i,j))
                            seen.add((i,j))
                            q.insert(0, (i,j))
                    
            if capture:
                for x,y in to_be_captured:
                    board[x][y] = "X"
                
                 
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen and board[r][c] == "O":
                    bfs(r,c)
          