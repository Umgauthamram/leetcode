# LeetCode 526

# input
# 2

# output
# 2

def countArrangement(n):
    visited = [False] * (n + 1)
    
    def backtrack(index):
        if index>n:
            return 1

        count = 0
        for num in range(1,n+1):
            if not visited[num] and (num % index == 0 or index % num ==0):
                visited[num] = True
                count +=backtrack(index+1)
                visited[num] = False

        return count
    return backtrack(1)


if __name__ == "__main__":
    n = int(input())
    print(countArrangement(n))