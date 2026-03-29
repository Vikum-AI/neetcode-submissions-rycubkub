class Solution:
    def merge(self, list1, list2):
        l1 = l2 = 0
        res = []

        while l1 < len(list1) and l2 < len(list2):
            if list1[l1] <= list2[l2]:
                res.append(list1[l1])
                l1 += 1

            else:
                res.append(list2[l2])
                l2 += 1

        res.extend(list1[l1:])
        res.extend(list2[l2:])

        return res


    def merge_sort(self, arr):
        n = len(arr) 

        if n <= 1:
            return arr

        mid = n // 2

        arr1 = self.merge_sort(arr[:mid])
        arr2 = self.merge_sort(arr[mid:])

        return self.merge(arr1, arr2)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
        