class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.constructPrefix()

    def constructPrefix(self):
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

        self.prefix_matrix = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]

        for r in range(1, self.rows + 1):
            for c in range(1, self.cols + 1):
                self.prefix_matrix[r][c] = self.prefix_matrix[r-1][c] + self.prefix_matrix[r][c-1] + self.matrix[r-1][c-1] - self.prefix_matrix[r-1][c-1]

        return self.prefix_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = (self.prefix_matrix[row2 +1][col2 +1] - 
        self.prefix_matrix[row1][col2 +1] -
        self.prefix_matrix[row2 +1][col1] +
        self.prefix_matrix[row1][col1]
        )

        return result
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)