class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        count = 0

        intervals.sort(key=lambda k: k[0])

        while count < len(intervals):
            start, end = intervals[count]

            while count < len(intervals) - 1 and (intervals[count+1][0] <= end):
                end = max(end, intervals[count+1][1])
                start = min(start, intervals[count+1][0])
                count += 1

            res.append((start, end))
            count += 1

        return res