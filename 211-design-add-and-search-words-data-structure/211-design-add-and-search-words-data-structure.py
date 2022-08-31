class Node():
    def __init__(self, val=None):
        self.val = val
        self.end = False
        self.children = {}

# we use a Trie(prefix tree) data structure to hold the words.
# more on tries here https://en.wikipedia.org/wiki/Trie
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
                    # this matches anything so we have to check every posible sufix down the tree
                    # to find a match
                    #loop through all children and call dfs for all of them
                    for child in curr.children.values():
                        if dfs(child, word[i+1:]):
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