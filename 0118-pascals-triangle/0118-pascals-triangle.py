class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            row = [1] * (i+ 1)

            for k in range(1, i):
                row[k]=triangle[i-1][k-1] + triangle[i-1][k]

            triangle.append(row)

        return triangle