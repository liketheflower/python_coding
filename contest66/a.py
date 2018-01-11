class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        if not words: return ""
        #words_dict = dict(words)
        label = []
        for word in words:
            for i in range(0,len(S)-len(word)+1):
                #print S[i:i+len(word)]
                if S[i:i+len(word)] == word:
                 
                    label.append((i,i+len(word)))
                    if word=='zgtud':
                        print label

        label.sort()
        #print "label",label
        if not label: return S
        left, right = label[0][0],label[0][1]
        final_res =[]
        for i in range(1,len(label)):
            if label[i][0]<=right:
                right =max(right, label[i][1])
            else:
                final_res.append((left, right))
                left,right = label[i][0],label[i][1]
        final_res.append((left, right))
        
        if not final_res: return S
        left_ans = [i for i,j in final_res]
        right_ans =[j for i,j in final_res]
        left_ans=left_ans[::-1]
        right_ans=right_ans[::-1]
        l=left_ans.pop()
        r=right_ans.pop()
        fin_ans=''
        for i in range(len(S)+1):
            if i==l:
                fin_ans+='<b>'
                if left_ans:
                    l = left_ans.pop()
            if i==r:
                fin_ans+='</b>'
#                print right_ans
                if right_ans:
                    r=right_ans.pop()
            if i!=len(S):
                fin_ans+=S[i]
        if right_ans:
            fin_ans+='</b>'
        return fin_ans



words=["ccb","b","d","cba","dc"]
S="eeaadadadc"
words=["di","r","buhozb","lofjmyjj","qagllw","zzuid","loyugfh","w","hcfg","ttd","vjqigvx","u","mhbivve","x","nzbvyfzx","zs","j","zgtud","zm","huevyex","szwigrlwzm","vlrjmobu","b","h","gcmdgyv","anyfelm","vtcejv","myjjzn","jznnj","awcxmjn","lw","sju","szszwigrl","eze","ffikvecua","bklrhsju","gyazwel","pdhnsxsod","zn","rhsjus","zk","gctgu","vzndt","mfd","jlws","j","zxgaudyo","apa","znvixpdh","tgubzczgt"]
S="wwcyuaqzgtudmpjkluqoseslygywzkixjqghsocvjqigvxwqloyugfhcjscjghqmiglgyazwelshzapaezqgmcmrmfrfzttdgquizyducbvxzzuiddcnwuaapdunzlbagnifndbjyalqqgbramhbivvervxrtcszszwigrlwzmuteyswzagudtpvlrjmobuhozbghkhvoxawcxmjnazlqlkqqqnoclufgkovbokvkoezeknwhcfgcenvaablpvtcejvzndtzncrelhedwlwiqgdbdgctgubzczgtovufncicjlwsmfdcrqeaghuevyexqdhffikvecuazrelofjmyjjznnjdkimbklrhsjusbstqhvlejtjcczqnzbvyfzxgaudyosckysmminoanjmbafhtnbrrzqagllwxlxmjanyfelmwruftlzuuhbsjexoobjkmymlitiwjtdxscotzvznvixpdhnsxsodieatipiaodgcmdgyv"
a=Solution()
print a.boldWords(words, S)
