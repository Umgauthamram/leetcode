class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        n =len(edges)
        scores = [0]*n

        for src, dest in enumerate(edges):
            scores[dest] +=src

        best = 0
        maxScores = -1

        for node in range(n):
            if scores[node]>maxScores:
                maxScores = scores[node]
                best = node
        return best