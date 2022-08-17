class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for w in word:
            if w not in temp.children:
                temp.children[w] = TrieNode()
            temp = temp.children[w]
        temp.end = True
                
    def search(self, word: str) -> bool:
        temp = self.root
        for w in word:
            if w not in temp.children:
                return False
            temp = temp.children[w]
        return temp.end

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for p in prefix:
            if p not in temp.children:
                return False
            temp = temp.children[p]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)