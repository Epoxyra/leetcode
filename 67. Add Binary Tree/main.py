class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = (len(b) - len(a))*"0" + a
        elif len(b) < len(a):
            b = (len(a) - len(b))*"0" + b
        stock = 0
        res = []
        a = a[::-1]
        b = b[::-1]
        for i in range(len(a)):
            res.append(str((int(a[i]) + int(b[i]) + stock) % 2))
            stock = (int(a[i]) + int(b[i]) + stock) // 2
        if stock:
            res.append("1")
        res = res[::-1]
        return "".join(res)

a = "11"
b = "1"
sol = Solution()
res = sol.addBinary(a, b)
print(res)