class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1

        boats = 0

        while l < r:
            if people[l] + people[r] <= limit:
                print(people[l], people[r])
                boats += 1
                l += 1
                r -= 1
                continue

            boats += 1
            r -= 1


        if people[l:r+1]:
            boats += 1

        return boats
        