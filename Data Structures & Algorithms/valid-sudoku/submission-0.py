class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            seen = set()
            for value in row:
                if value != ".":
                    if value in seen:
                        return False
                    seen.add(value)
        
        for col in range(9):
            seen = set()
            
            for row in range(9):
                value = board[row][col]

                if value != ".":
                    if value in seen:
                        return False
                    seen.add(value)

        for start_row in range(0, 7, 3):
            for start_col in range(0, 7, 3):
                seen = set()

                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        value = board[r][c]
                    
                        if value != ".":
                            if value in seen:
                                return False
                            seen.add(value)
        return True




