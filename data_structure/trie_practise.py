import collections

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode) # maps from Character -> TrieNode
        self.is_word = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        print 'self.root',self.root
        for letter in word:
            current = current.children[letter]
            print letter, current,current.children.keys(), current.children.values(), current.is_word
            
        current.is_word = True
        print "end",current, current.is_word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        
        for letter in word:
            current = current.children.get(letter)
            if not current:
                return False
        
        return current.is_word
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        
        for letter in prefix:
            current = current.children.get(letter)
            if not current:
                return False
        return True
    def show(self):
        cur = self.root
        open_list = cur.children.keys()
        while open_list:
           if cur.is_word:
               cur=self.root
           ch = open_list.pop()
           print ch
           cur = cur.children[ch]
           open_list.extend(cur.children.keys())

# Your Trie object will be instantiated and called as such:
obj = Trie()
print obj.insert('love')
print obj.insert('large')
obj.show()
#print obj.search('love')
#print obj.startsWith('l')
# param_2 = obj.search(word)

# param_3 = obj.startsWith(prefix)
