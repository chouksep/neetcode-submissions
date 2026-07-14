# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)

    def mergeSortHelper(self, pairs, left, right):
        if right - left + 1 <= 1:
            return pairs
        mid = (left+ right) // 2
        self.mergeSortHelper(pairs, left, mid)
        self.mergeSortHelper(pairs, mid+1, right)
        self.merge(pairs, left, mid, right)
        return pairs

    def merge(self, arr, left, mid, right):
        L = arr[left:mid+1]
        R = arr[mid+1:right+1]

        i = 0 # for L sub-arr
        j = 0 # for R sub-arr
        k = left # for arr

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i  < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j  < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


