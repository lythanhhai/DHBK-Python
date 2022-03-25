class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max = arr[0]
        index = -1
        for i in range(0, len(arr)):
            if max < arr[i]:
                max = arr[i]
                index = i
        return index
        