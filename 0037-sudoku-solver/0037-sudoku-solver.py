class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_spaces = []

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                box_id = (row // 3) * 3 + (col // 3)
                if value != ".":
                    rows[row].add(value)
                    columns[col].add(value)
                    boxes[box_id].add(value)

                else:
                    empty_spaces.append((row, col))

        def sudoku(idx):
            if idx >= len(empty_spaces):
                return True

            row, col = empty_spaces[idx]
            box_id = (row // 3)* 3 + (col // 3)
            for i in "123456789":
                if i not in rows[row] and i not in columns[col] and i not in boxes[box_id]:
                    board[row][col] = i
                    rows[row].add(i)
                    columns[col].add(i)
                    boxes[box_id].add(i)

                    if sudoku(idx + 1):
                        return True

                    board[row][col] = "."
                    rows[row].remove(i)
                    columns[col].remove(i)
                    boxes[box_id].remove(i)

            return False

        sudoku(0)
        