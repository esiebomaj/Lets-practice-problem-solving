class Trie():
    def __init__(self, val=None):
        self.val = val
        self.end = 0
        self.children = {}
        self.count = 0
        
    def addWord(self, word):
        curr = self
        
        for i in range(len(word)):
            char = word[i]
            if char not in curr.children:
                curr.children[char] = Trie(char)
            
            curr = curr.children[char]
            curr.count += 1
            
        curr.end += 1
        
    def removeWord(self, word):
        curr = self
        for i in range(len(word)):
            char = word[i]
            if char in curr.children:
                curr.children[char].count -= 1
            curr = curr.children[char]
        curr.end -= 1
        


class Solution:
    
    def dfs(self, r, c, board, node, path, seen):
        
        if (r < 0) or\
        (c < 0) or \
        (r >= len(board)) or\
        (c >= len(board[0])) or \
        ((r,c) in seen) or \
        (board[r][c] not in node.children) or\
        (node.children[board[r][c]].count <= 0) or\
        (len(path) > self.maxLen):
            
            return False
        
        path = path + board[r][c]
        
        if node.children[board[r][c]].end >= 1:
            self.res.append(path)
            self.root.removeWord(path)
            
        
        seen.add((r,c))
        for x,y in [[1,0], [-1,0],  [0,1], [0,-1]]:
            self.dfs(r+x, c+y, board, node.children[board[r][c]], path, seen)
        seen.remove((r,c))
        
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = Trie()
        self.maxLen = float(-inf)
        
        for word in words:
            self.maxLen = max(self.maxLen, len(word))
            self.root.addWord(word)
            
        self.res = []
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.dfs(row, col, board, self.root, "", set())
        return self.res
        