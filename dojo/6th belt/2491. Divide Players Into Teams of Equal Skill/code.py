class Solution(object):
    def dividePlayers(self, skill):

        skill.sort()
        total_sum = skill[0] +skill[-1]
        total_chem = 0
        l,r = 0,len(skill)-1

        while l<r:
            if skill[l]+skill[r] != total_sum:
                return -1
            total_chem += skill[l] *skill[r]
            l +=1
            r -=1
        return total_chem
        

# LC 2491
# Input: [3,2,5,1,3,4]
# Output: 22