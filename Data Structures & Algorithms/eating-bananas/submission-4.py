class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # eating rate 1-h (k)

        l, r = 1, max(piles)
        k = r

        # [1, 2, 3, 4, 5]

        while l <= r:
            mid = (l + r) // 2

            time = 0

            for pile in piles:
                time += math.ceil(float(pile) / mid)

            if time > h:
                l = mid + 1
            else:
                r = mid - 1
                k = min(k, mid)

        return k

