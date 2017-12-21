class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
           return []
        a = 'qwertyuiop'
        b=  'asdfghjkl'
        c=  'zxcvbnm'
        res = []
        for word in words:
           good = True
           if not word:
              continue
           if word[0].lower() in a: 
              for w in word:
                  if w.lower() not in a:
                      good = False
                      break
              if good:
                  res.append(word)
           elif word[0].lower() in b:
              for w in word:
                 if w.lower() not in b:
                      good = False
                      break
              if good:
                  res.append(word)
           else:
              for w in word:
                  if w.lower() not in c:
                      good = False
                      break
              if good:
                  res.append(word)
        return res


a = Solution()
s = ["Hello", "Alaska", "Dad", "Peace"]
print a.findWords(s)
