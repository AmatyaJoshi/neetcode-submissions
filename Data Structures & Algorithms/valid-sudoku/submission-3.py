class Solution:
    def check(self, values):
        seen = set()

        for value in values:
            if value != ".":
                    if value in seen:
                        return False
                    seen.add(value)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            if not self.check(row):
                return False
        
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.check(column):
                return False

        for start_row in range(0, 7, 3):
            for start_col in range(0, 7, 3):
                box = [
                    board[r][c]
                    for r in range(start_row, start_row + 3)
                    for c in range(start_col, start_col + 3)
                ]

                if not self.check(box):
                    return False    
        return True