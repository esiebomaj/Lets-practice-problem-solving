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
        to_be_captured = set()
        
        rows = len(board)
        cols = len(board[0])
        
        def bfs(r, c):
            
            q = [(r,c)]
            curr_to_be_captured = set()
            curr_to_be_captured.add((r,c))
            capture = True
            
            while q:
                
                curr = q.pop()
                seen.add(curr)
                
                for dy, dx in [[1,0], [-1,0], [0,1], [0,-1]]:
                    i,j = curr[0]+dy, curr[1]+dx
                    print(i,j)
                    if i < 0 or i >= rows or j < 0 or j >= cols:
                        print("out of bounds", i,j)
                        # if out of bounds
                        capture = False
                    else:
                        # not out of bounds
                        if board[i][j] == "O" and (i,j) not in seen:
                            curr_to_be_captured.add((i,j))
                            seen.add((i,j))
                            q.insert(0, (i,j))
                    
            if capture:
                for x,y in curr_to_be_captured:
                    board[x][y] = "X"
                # to_be_captured.update(curr_to_be_captured)
                
                 
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen and board[r][c] == "O":
                    print('entry',r,c)
                    bfs(r,c)
                    
        print(to_be_captured)
        
        [["X","O","X"],
         ["O","X","O"],
         ["X","O","X"]]
        
        
        [["X","X","X"],
         ["X","X","O"],
         ["X","O","X"]]
        
        