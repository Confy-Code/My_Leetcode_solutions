class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        # INITIALIZING AN EMPTY BOARD
        board = [["." for _ in range(n)] for _ in range(n)]
        answer = []

        def helper(row):
            if row == n:
                # Deep copy to avoid any changes
                copy = ["".join(b) for b in board]
                answer.append(copy)
                return


            for col in range(n):
                if self.safePlace(board, row, col, n):
                    board[row][col] = "Q"
                    helper(row + 1)

                    # Once the loop runs out, we will BACKTRACK
                    # We replace the existing Q with an empty space
                    board[row][col] = "."
        helper(0)
        return answer

    # This funtion tests safe places
    def safePlace(self, board, row, col, n):

        # TESTING VERTICALLY (SAME COLUMN)
        for idx in range(n):
            if board[idx][col] == "Q":
                return False

        # TESTING HORIZONTALLY (SAME ROW)
        for idx in range(n):
            if board[row][idx] == "Q":
                return False

        # TESTING LEFT DIAGONAL
        r, c = row, col
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            
            r -= 1
            c -= 1

        #TESTING RIGHT DIAGONAL
        r, c = row, col
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False

            r -= 1
            c += 1

        return True