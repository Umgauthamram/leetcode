class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):

        n = len(customers)
        alr = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        cur =0

        for i in range(minutes):
            if grumpy[i] == 1:
                cur += customers[i]
        max_extra = cur

        for i in range(minutes,n):
            if grumpy[i] == 1:
                cur += customers[i]
            if grumpy[i-minutes] == 1:
                cur -=customers[i-minutes]
            max_extra = max(max_extra,cur)

        return alr+max_extra



# LC 1052
# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
# Output: 16