# https://leetcode.com/problems/base-7/
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(num)
        sign = ''
        if num < 0:
            sign = '-'
            num *= (-1)
        res = []
        result = ''
        while num >= 7:
            x = num // 7
            res.append(num - x * 7)
            num = x
        res.append(num)
        res = res[::-1]
        for el in res:
            result += str(el)
        result = sign + result
        return result