class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        def find_zero(x, y, covered = None):
            if covered is None:
                covered = set()
            covered.add((x, y))
            paths = []
            if mat[x][y] == 0:
                return 0
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < m and 0 <= y + dy < n and (x + dx, y + dy) not in covered:
                    paths.append(1 + find_zero(x + dx, y + dy, covered.copy()))
            if paths:
                return min(paths)
            else:
                return float('inf')
        for i in range(m):
            for j in range(n):
                res[i][j] = find_zero(i, j)
        return res