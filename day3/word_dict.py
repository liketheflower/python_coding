import collections

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word:
            self.word_dict[len(word)].append(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        
        for v in self.word_dict[len(word)]:
            found = True
            for i, char in enumerate(word):
                if char != v[i] and char !='.':
                    found = False
                    break
                    
            if found:
                return True
        
        return False
        


# Your WordDictionary object will be instantiated and called as such:
word = "love"
obj = WordDictionary()
print obj.word_dict
obj.addWord(word)
obj.addWord(word)
obj.addWord(word)
obj.addWord(word)
obj.addWord(word)
obj.addWord(word)
obj.addWord(word)
obj.addWord(word)
print obj.word_dict
obj.addWord('have')
print obj.word_dict
obj.addWord('friend')
print obj.word_dict
param_2 = obj.search('h.te')


