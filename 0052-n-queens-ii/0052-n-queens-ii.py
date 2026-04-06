class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = [["." for _ in range(n)] for _ in range(n)]
        answer = []

        def helper(row):
            if row == n:
                copy = ["".join(b) for b in board]
                answer.append(copy)
                return

            for col in range(n):
                if self.safePlace(board, row, col, n):
                    board[row][col] = "Q"
                    helper(row + 1)

                    # BACKTRACKING
                    board[row][col] = "."

        helper(0)
        return len(answer)

    def safePlace(self, board, row, col, n):

        #Vertical test
        for idx in range(n):
            if board[idx][col] == "Q":
                return False

        # Horizontal check
        for idx in range(n):
            if board[row][idx] == "Q":
                return False

        # Left diagonal check
        r, c = row, col
        while r >= 0  and c >= 0:
            if board[r][c] == "Q":
                return False

            r -= 1
            c -= 1

        # Right diagonal check
        r, c = row, col
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False

            r -= 1
            c += 1

        return True