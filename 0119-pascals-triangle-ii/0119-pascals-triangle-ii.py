class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        previous_row = self.getRow(rowIndex - 1)
        current_row = [1]

        for idx in range(1, rowIndex):
            current_row.append(previous_row[idx] + previous_row[idx - 1])
        
        current_row.append(1)
        return current_row



        