import string
import random
class Solution:
    def findWordsRe(self, words):
        return list(filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words))

    def findWordsRe2(self, words):
        return [word for word in words if re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match(word)]

    def findWordsSet(self, words):
        row1 = set('qwertyuiopQWERTYUIOP')
        row2 = set('asdfghjklASDFGHJKL')
        row3 = set('zxcvbnmZXCVBNM')
        return list(filter(lambda x: set(x).issubset(row1) or set(x).issubset(row2) or set(x).issubset(row3), words))

    def findWordsSet2(self, words):
        row1 = set('qwertyuiopQWERTYUIOP')
        row2 = set('asdfghjklASDFGHJKL')
        row3 = set('zxcvbnmZXCVBNM')
        return [word for word in words if set(word).issubset(row1) or set(word).issubset(row2) or set(word).issubset(row3)]

import timeit, re, random, string

words = [''.join(random.choices(string.ascii_lowercase, k=5)) for i in range(1000)]
print(timeit.timeit(lambda: Solution().findWordsRe(words), number=1000), "(re with filter)")
print(timeit.timeit(lambda: Solution().findWordsRe2(words), number=1000), "(re with list comprehension)")
print(timeit.timeit(lambda: Solution().findWordsSet(words), number=1000), "(set with filter)")
print(timeit.timeit(lambda: Solution().findWordsSet2(words), number=1000), "(set with list comprehension)")
