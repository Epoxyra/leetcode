from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[-1 for _ in range(n)] for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))
        neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in neighbours:
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        if mat[x + dx][y + dy] == 1 and res[x + dx][y + dy] == -1:
                            res[x + dx][y + dy] = distance
                            queue.append((x + dx, y + dy))
        return res