class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        nr = len(matrix)
        nc = len(matrix[0])

        cr, cc =  0, nc -1

        while cr < nr and cc >= 0:
            val = matrix[cr][cc] 
            if  val == target :
                return True
            if val > target:
                cc -= 1
            else:
                cr += 1
        return False
        