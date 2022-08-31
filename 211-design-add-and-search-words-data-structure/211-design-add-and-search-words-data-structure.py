class Node():
    def __init__(self, val=None):
        self.val = val
        self.end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()
               
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in curr.children:
                curr.children[char] = Node(char)
                
            curr = curr.children[char]
            
        curr.end = True
                  
    
    def search(self, word: str) -> bool:
        
        def dfs(trie, word):
            curr = trie
            
            for i in range(len(word)):
                char = word[i]
                if char == ".":
                    # for loop and call this method for all of them
                    for child in curr.children:
                        if dfs(curr.children[child], word[i+1:]):
                            return True
                    return False

                else:
                    if char not in curr.children:
                        return False
                    
                    curr = curr.children[char]
                    
                        
            return curr.end
        
        return dfs(self.root, word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)