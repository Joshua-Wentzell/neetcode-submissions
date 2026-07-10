from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        these_squares = defaultdict(set)
        these_counts = defaultdict(int)

        for r in range(9):
            this_row_set = set()
            num_row_count = 0
            this_col_set = set()
            num_col_count = 0

            if r > 0 and r % 3 == 0:
                for key, value in these_squares.items():
                    if len(these_squares[key]) < these_counts[key]:
                        print("4")
                        return False
                these_squares = defaultdict(set)
                these_counts = defaultdict(int)

            for j in range(9):
                if board[r][j] != ".":
                    if board[r][j] not in "123456789":
                        return False
                    this_row_set.add(board[r][j])
                    num_row_count += 1
                    these_squares[j//3].add(board[r][j])
                    these_counts[j//3] += 1
                if board[j][r] != ".":
                    if board[j][r] not in "123456789":
                        return False
                    this_col_set.add(board[j][r])
                    num_col_count += 1

            if len(this_row_set) < num_row_count or len(this_col_set) < num_col_count:
                return False
        return True
        

