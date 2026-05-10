class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)

        def timeTaken(k):
            hrs = 0

            for pile in piles:
                hrs += math.ceil(pile / k)
            
            return hrs

        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            tt = timeTaken(mid)

            if tt <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res

        