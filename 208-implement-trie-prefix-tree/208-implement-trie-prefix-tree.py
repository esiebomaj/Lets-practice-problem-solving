# Brute force solution
# class Trie:

#     def __init__(self):
#         self.data = set()
        

#     def insert(self, word: str) -> None:
#         self.data.add(word)
        

#     def search(self, word: str) -> bool:
#         return word in self.data
        
    
#     def startsWith(self, prefix: str) -> bool:
#         for string in self.data:
#             if string[:len(prefix)] == prefix:
#                 return True
#         return False
    
    
# optimized solution
class Node():
    def __init__(self, val, end=False):
        self.val = val
        self.end = end
        self.children = {} # list of nodes
        
        
class Trie:

    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            char = word[i]
            
            if char not in curr.children:
                curr.children[char] = Node(char)
                
            curr = curr.children[char]
        curr.end = True
                       

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            char = word[i]
            
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
            
        return curr.end
            
            
            
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
            
        return True       


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)