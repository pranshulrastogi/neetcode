class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        p, q = 0, (m*n)-1

        def get_row_col(mid):
            row = mid // n
            col = mid % n
            return row, col
        while p <= q:
            mid = (p+q)//2
            row, col = get_row_col(mid)
            value = matrix[row][col]
            if value > target:
                q = mid - 1
            elif value == target:
                return True
            else:
                p = mid + 1
        return False