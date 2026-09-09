class Solution(object):
    def combinationSum3(self, k, n):

        res = []
        def backtrack(start,path,target):
            if len(path) == k:
                if target == 0:
                    res.append(list(path))
                return
            for i in range(start,10):
                if i >target:
                    break
                path.append(i)
                backtrack(i+1,path,target-i)
                path.pop()
        backtrack(1,[],n)
        return res
        

# LC 216
# Input: k = 3, n = 7
# Output: [[1,2,4]]