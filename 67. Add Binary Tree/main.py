class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = (len(b) - len(a))*"0" + a
        elif len(b) < len(a):
            b = (len(a) - len(b))*"0" + b
        stock = False
        res = []
        a = a[::-1]
        b = b[::-1]
        for i in range(len(a)):
            if stock:
                if int(a[i]) and not int(b[i]) or int(b[i]) and not int(a[i]):
                    stock = True
                    res.append("0")
                else:
                    stock = True if int(a[i]) and int(b[i]) else False
                    res.append("1")
            else:
                print(int(a[i]), int(b[i]))
                if int(a[i]) and not int(b[i]) or int(b[i]) and not int(a[i]):
                    stock = False
                    res.append("1")
                else:
                    stock = True if int(a[i]) and int(b[i]) else False
                    res.append("0")
        if stock:
            res.append("1")
        res = res[::-1]
        return "".join(res)

a = "11"
b = "1"
sol = Solution()
res = sol.addBinary(a, b)
print(res)