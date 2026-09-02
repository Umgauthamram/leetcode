# LeetCode 2597
# input
# 3 2
# 2 4 6

# output
#4


from collections import defaultdict
from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        count = defaultdict(int)

        def backtrack(index:int)->int:
            if index == len(nums):
                return 1

            total = backtrack(index + 1)
            val = nums[index]
            if count[val-k] == 0 == count[val+k] == 0:
                count[val] +=1
                total +=backtrack(index+1)
                count[val] -= 1
            return total
        return backtrack(0)-1

if __name__ == "__main__":
    n, k = map(int, input().split()) 
    nums = list(map(int, input().split())) 

    solution = Solution()
    result = solution.beautifulSubsets(nums, k)
    print(result)


