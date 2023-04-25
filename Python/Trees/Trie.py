ALPHABET_SIZE = 26
class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children = [None for i in range(ALPHABET_SIZE)]
    
class Trie:
    def __init__(self):
        self.root = self.getNode()
    def getNode(self):
        return TrieNode()
    def _charToIndex(self, chr):
        return ord(chr)-ord('a')
    def insert(self, key):
        length = len(key)
        pCrawl = self.root
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True
    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEndOfWord
    def isEmpty(self):
        return self._isEmpty(self.root)
    def delete(self, key):
        self._delete(self.root, key)
    def _isEmpty(self, root):
        for i in range(ALPHABET_SIZE):
            if root.children[i] is not None: return False
        return True
    def _delete(self,root, key,depth=0):
        if depth == len(key):
            if root.isEndOfWord is False: raise Exception("Item not found!")
            root.isEndOfWord = False
            return
        index = self._charToIndex(key[depth])
        if root.children[index] is None: raise Exception("Item not found")
        self._delete(root.children[index], key, depth+1)
        
        
            
    

keys = ["the","a","there","anaswe","any","by","their"]
output = ["Not present in trie","Present in trie"]
t = Trie()
for key in keys: t.insert(key)
print(f"{'the'} ---- {output[t.search('the')]}")
print(f"{'these'} ---- {output[t.search('these')]}")
print(f"{'their'} ---- {output[t.search('their')]}")
print(f"{'thaw'} ---- {output[t.search('thaw')]}")
t.delete("by")
print("{} ---- {}".format("by",output[t.search("by")]))
 
                