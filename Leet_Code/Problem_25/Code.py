class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        count = 0
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if j == len(nums2) - 1:
                    res.append(-1)
                    break
                else:
                    if nums1[i] == nums2[j]:
                        for k in range(j + 1, len(nums2)):
                            if nums2[j] < nums2[k]:
                                res.append(nums2[k])
                                count += 1
                                break
                            else:
                                continue
                        if count > 0:
                            count = 0
                            break
                        
        return res