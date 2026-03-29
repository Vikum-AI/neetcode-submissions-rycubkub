class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
                return 0
        
        for j in range(len(stones)):
            if len(stones) == 0:
                return 0

            if len(stones) == 1:
                return stones[0]
            
            h1 = 0 # first highest
            h2 = 1 # second highest

            if stones[h2] > stones[h1]:
                h1, h2 = h2, h1

            for i, stone in enumerate(stones):
                if i < 2:
                    continue

                if stone > stones[h1]:
                    h2, h1 = h1, i
                elif stone > stones[h2]:
                    h2 = i

            print(stones[h1], stones[h2])

            diff = stones[h1] - stones[h2]

            if diff:
                stones[h1] = diff
                del stones[h2]
            else:
                del stones[h2]
                del stones[h1]

            print(stones)

        return 0






