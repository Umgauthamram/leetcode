from typing import List

def three_sum_smaller(nums: List[int], target: int) -> int:
    nums.sort()
    count = 0
    n = len(nums)
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum < target:
                count += (right - left)
                left += 1
            else:
                right -= 1
                
    return count

if __name__ == "__main__":
    n, target = map(int, input().split())
    nums = list(map(int, input().split()))
    print(three_sum_smaller(nums, target))