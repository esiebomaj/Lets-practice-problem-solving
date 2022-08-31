class Trie:

    def __init__(self):
        self.data = set()
        

    def insert(self, word: str) -> None:
        self.data.add(word)
        

    def search(self, word: str) -> bool:
        return word in self.data
        

    def startsWith(self, prefix: str) -> bool:
        for string in self.data:
            if string[:len(prefix)] == prefix:
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)