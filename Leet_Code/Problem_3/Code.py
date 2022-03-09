class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        a = '{0:08b}'.format(x)
        b = '{0:08b}'.format(y)
        add = ""
        if len(a) < len(b):
            for i in range(0, len(b) - len(a)):
                add += "0"
            a = add + a
        elif len(a) > len(b):
            for i in range(0, len(a) - len(b)):
                add += "0"
            b = add + b
        for i in range(0, len(a)):
            if a[i] != b[i]:
                count += 1
        return count