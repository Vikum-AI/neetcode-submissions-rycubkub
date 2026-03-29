"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def merge(self, left, right):
        output = []

        while left and right:
            min_num = left.pop(0) if left[0].start <= right[0].start else right.pop(0)
            output.append(min_num)

        output.extend(left)
        output.extend(right)

        return output

    def merge_sort(self, arr):
        n = len(arr)

        if n <= 1:
            return arr

        mid = n // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals_sorted = self.merge_sort(intervals)
        
        for i, inter in enumerate(intervals_sorted):
            if i + 1 >= len(intervals_sorted):
                break

            start, end = inter.start, inter.end
            
            if intervals_sorted[i+1].start < end:
                return False

        return True

