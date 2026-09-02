# LeetCode 1802

# input 
# 4
# 2
# 6

# output 
# 2

def maxValue(n: int, index: int, maxSum: int) -> int:
    def get_sum(target, count):
        if target > count:
            return (target + (target - count + 1)) * count // 2
        else:
            ones = count - target
            return (target + 1) * target // 2 + ones

    left, right = 1, maxSum
    result = 1

    while left <= right:
        mid = (left + right) // 2
        
        left_sum = get_sum(mid - 1, index)
        right_sum = get_sum(mid - 1, n - 1 - index)
        total_sum = mid + left_sum + right_sum
        
        if total_sum <= maxSum:
            result = mid
            left = mid + 1  
        else:
            right = mid - 1 

    return result




if __name__ == "__main__":
    n = int(input())     
    index = int(input())     
    maxSum = int(input())   

    result = maxValue(n, index, maxSum)
    print(result)