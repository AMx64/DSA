class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        idx1, idx2 = 0, 0
        arr = []
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] <= nums2[idx2]:
                arr.append(nums1[idx1])
                idx1 += 1
            else:
                arr.append(nums2[idx2])
                idx2 += 1

        if idx2 < len(nums2):
            arr.extend(nums2[idx2:])
        else:
            arr.extend(nums1[idx1:])
        n = len(arr)
        if n%2 == 0:
            return (arr[n//2 -1] +arr[n//2]) / 2
        else:
            return arr[n//2] 
            