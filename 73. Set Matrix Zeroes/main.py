class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row_contains_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_contains_zero = any(matrix[i][0] == 0 for i in range(m))

        # Store the fact that a line/column contains a zero is the first row/column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set all the zeros according to the first column and line
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Set zeros in the first column or line if a zero was there initially
        if first_col_contains_zero:
            for i in range(m):
                matrix[i][0] = 0
        if first_row_contains_zero:
            for j in range(n):
                matrix[0][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol = Solution()
sol.setZeroes(matrix=matrix)
        