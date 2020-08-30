class Solution():
    def commonsubstrings(self,sentence1, sentence2):
        sen1 = sentence1.split(' ')
        sen1.append('#')
        sen2 = sentence2.split(' ')
        sen2.append('!')
        n = len(sen1)
        m = len(sen2)
        res = []
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if self.sameword(sen1[i],sen2[j]):
                    dp[i+1][j+1]=dp[i][j]+1

                if dp[i+1][j+1]==0 and dp[i][j]>=3:
                    commstr = ' '.join(sen1[i-dp[i][j]:i])
                    res.append(commstr)
       
        return res
    def sameword(self,word1,word2):
        i = len(word1)
        j = len(word2)
        if i != j:
            return False
        for k in range(i):
            if word1[k] != word2[k]:
                return False
        return True
a = Solution()
s1 = "today is sunny and okay I feel yes so happy"
s2 = "tomorrow is sunny and that makes today is sunny and okay me feel yes so happy too"
print(a.commonsubstrings(s1,s2))