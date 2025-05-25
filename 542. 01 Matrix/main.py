from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    q.append((i, j))
                    covered = []
                    path_len = 0
                    while q:
                        for _ in range(len(q)):
                            x, y = q.popleft()
                            if mat[x][y] == 0:
                                res[i][j] = path_len
                                q.clear()
                                break
                            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                                if 0 <= x + dx < m and 0 <= y + dy < n and (x + dx, y + dy) not in covered:
                                    q.append((x + dx, y + dy))
                                    covered.append((x, y))
                        path_len += 1
        return res