class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        p1 = 0
        p2 = 1

        while p2 < len(intervals):
            cur_s, cur_e = intervals[p1]
            next_s, next_e = intervals[p2]

            # overlapping
            if next_s <= cur_e:
                new_s = min(cur_s, next_s)
                new_e = max(cur_e, next_e)

                intervals[p1] = [new_s, new_e]
                del intervals[p2]
                continue

            p1 += 1
            p2 += 1

        return intervals
            
