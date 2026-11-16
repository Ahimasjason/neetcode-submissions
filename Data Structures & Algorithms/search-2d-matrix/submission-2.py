class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        nr = len(matrix)
        nc = len(matrix[0])
        lo, hi  = 0, (nr * nc ) - 1
        while lo <= hi:

            mid = lo + (hi - lo) // 2
            r = mid // nc
            c = mid % nc
            v = matrix[r][c]
            if v == target:
                return True
            if target > v:
                lo = mid + 1
            else:
                hi = mid - 1

        

        return False
        