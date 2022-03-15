from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[int]:
        res_convert = []
        res_invert = []
        for sub in image:
            sub1 = sub[::-1]
            res_convert.append(sub1)
        
        for sub in res_convert:
            sub1 = []
            for item in sub:
                if item == 0:
                    sub1.append(1)
                else:
                    sub1.append(0)
            res_invert.append(sub1)
        return res_invert