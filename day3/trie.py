class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = {}
        print 'init the trie', self.word_dict 

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        d = self.word_dict
        print'1', d
        for c in word:
            print 'c',c
            if c not in d:
                d[c] = {}
            d = d[c]
            print '2', d
        d['W'] = {}
        print '3',d
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        d = self.word_dict
        for c in word:
            if c not in d:
                return False
            d = d[c]
        return 'W' in d
            
        
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        d = self.word_dict
        for c in prefix:
            if c not in d:
                return False
            d = d[c]
        return True
        


# Your Trie object will be instantiated and called as such:
word = 'hello'
prefix = 'hello'
obj = Trie()
obj.insert(word)
print '---------------------------------'
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)


