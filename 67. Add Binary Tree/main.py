class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        stock = 0
        res = []
        for i in range(max_len - 1, -1, -1):
            res.append(str((int(a[i]) + int(b[i]) + stock) % 2))
            stock = (int(a[i]) + int(b[i]) + stock) // 2
        if stock:
            res.append("1")
        res = res[::-1]
        return "".join(res)