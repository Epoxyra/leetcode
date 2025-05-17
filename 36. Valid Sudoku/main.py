class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        def find_doubles_in_sublist(nested_list: list[list[str]]) -> bool:
            for list in nested_list:
                value_counts = {}
                for value in list:
                    value_counts[value] = 1 + value_counts.get(value, 0)
                value_counts.pop(".")
                for key in value_counts.keys():
                    if value_counts[key] > 1:
                        return True

        # Check if lines are valid
        if find_doubles_in_sublist(board):
            return False

        # Check if columns are valid
        columns = [[line[i] for line in board] for i in range(len(board))]
        if find_doubles_in_sublist(columns):
            return False
        
        # Check if each of the 3x3 sub-boxes are valid
        subsquares = [[] for _ in range(9)]
        line_idx = 0
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for di in range(3):
                    for dj in range(3):
                        subsquares[line_idx].append(board[i + di][j + dj])
                line_idx += 1
        if find_doubles_in_sublist(subsquares):
            return False
        
        return True