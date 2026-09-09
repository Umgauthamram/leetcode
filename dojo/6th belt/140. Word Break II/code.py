class Solution(object):
    def wordBreak(self, s, word_dict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        word = set(word_dict)
        res=[]

        def backtrack(start,path):
            if start == len(s):
                res.append(" ".join(path))
                return
            for end in range(start+1,len(s)+1):
                prefix = s[start:end]
                if prefix in word:
                    path.append(prefix)
                    backtrack(end,path)
                    path.pop()
        backtrack(0,[])
        return res


# LC 140
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]