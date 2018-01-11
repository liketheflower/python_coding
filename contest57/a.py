import collections
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words : return ""
        #res = []
        words.sort(key=len)
        print words
        cur_length=1
        words_dict = collections.defaultdict(set)
        for i, word in enumerate (words):
            if i==0 and len(words[0])!=1: break
            if len(words[i])==1:
                words_dict[len(word)].add(word)
            if i>0 and len(words[i]) !=len(words[i-1]):
                if len(words[i])!=cur_length +1 or not words_dict[cur_length]:
                    break
                else:
                    cur_length+=1
                    if words[i][:-1] in words_dict[cur_length-1]:
                        #res.append(words[i])
                        print words[i], words_dict[cur_length-1],cur_length
                        words_dict[cur_length].add(words[i])
            if i>0 and len(words[i]) ==len(words[i-1]):
                    if words[i][:-1] in words_dict[cur_length-1]:
                        #res.append(words[i])
                        print words[i], words_dict[cur_length-1],cur_length
                        words_dict[cur_length].add(words[i])
        print words_dict
        if words_dict[cur_length]: 
            tem = list(words_dict[cur_length])
            tem.sort()
            return tem[0]
        elif cur_length ==1: return ""
        else:
            tem = list(words_dict[cur_length-1])
            tem.sort()
            return tem[0]



a = Solution()
words = ["a","banana","app","appl","ap","apply","apple"]
words1=["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]

print a.longestWord(words)
print a.longestWord(words1)
