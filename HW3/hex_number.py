class Node:
    def __init__(self, nxt, val):
        self.nxt = nxt
        self.val = val


class HexNumber:
    hex_to_decimal = {c: i for i, c in enumerate('0123456789ABCDEF')}
    decimal_to_hex = {i: c for i, c in enumerate('0123456789ABCDEF')}

    def __init__(self, num='0'):
        if num[0] == '-':
            raise ValueError('Negative number')
        for el in num:
            if el not in self.hex_to_decimal:
                raise ValueError('Not Hex Number')
        if not num.isupper and not num.isdigit():
            raise ValueError('Lowercase letters')
        num = list(num)
        for i in range(len(num) - 1, -1, -1):
            num[i] = Node(None, num[i])
            if i != len(num) - 1:
                num[i + 1].nxt = num[i]
        self.head = num[len(num) - 1]

    def add(self, add_num):
        saver = 0
        cur1 = self.head
        cur2 = add_num.head
        res_head = None
        res_tail = None
        while cur1 is not None or cur2 is not None:
            if cur1 is None:
                cur1 = Node(None, '0')
            if cur2 is None:
                cur2 = Node(None, '0')
            cur3 = self.hex_to_decimal[cur1.val] + self.hex_to_decimal[cur2.val]
            if cur3 < 16:
                cur3 += saver
                saver = 0
            if cur3 >= 16:
                cur3 = cur3 - 16 + saver
                saver = 1
            node = Node(None, self.decimal_to_hex[cur3])
            if res_head is None:
                res_head = node
                res_tail = res_head
            else:
                res_tail.nxt = node
                res_tail = node
            cur1 = cur1.nxt
            cur2 = cur2.nxt
        res_number = HexNumber()
        res_number.head = res_head
        return res_number

    def __str__(self):
        ans = []
        cur = self.head
        while cur is not None:
            ans.append(cur.val)
            cur = cur.nxt
        ans = ans[::-1]
        return ''.join(ans)


if __name__ == "__main__":
    num1 = HexNumber('41F')
    num2 = HexNumber('13')
    num3 = num1.add(num2)
    print(num3)
