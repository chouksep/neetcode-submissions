class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # pointer 1
        last_ele = m + n -1

        # Pointer 2 and 3, m, n
        while m >0 and n > 0:
            # since both are sorted list, element at last whichever
            # is greater will be the max element of the output list
            # hence at last index
            if nums1[m-1] > nums2[n-1]:
                nums1[last_ele] = nums1[m-1]
                m -= 1
            else:
                nums1[last_ele] = nums2[n-1]
                n -= 1
            last_ele -= 1
        
        # in nums1 are already sorted if remaining, 
        # but in nums2 if the element is left, that means merge is not complete

        while n > 0:
            nums1[last_ele] = nums2[n-1]
            n -= 1
            last_ele -= 1
        