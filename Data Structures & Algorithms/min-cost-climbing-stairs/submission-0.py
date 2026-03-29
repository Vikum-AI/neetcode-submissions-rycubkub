class Solution:
    def minCostClimbingStairs(self, cost: List[int], n=None) -> int:
        for i in range(len(cost) - 1, -1, -1):
            if i >= len(cost) - 2:
                continue

            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[0], cost[1])