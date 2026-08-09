class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row binary-search
        r, c = len(matrix), len(matrix[0])
        Lr, Rr = 0, r - 1
        while Lr <= Rr:
            Mr = (Lr + Rr) // 2
            if matrix[Mr][0] <= target <= matrix[Mr][c-1]:
                break
            elif target < matrix[Mr][0]:
                Rr = Mr - 1
            elif target > matrix[Mr][c-1]:
                Lr = Mr + 1
        print(Mr)
        # col binary-search
        Lc, Rc = 0, c - 1
        while Lc <= Rc:
            Mc = (Lc + Rc) // 2
            if matrix[Mr][Mc] == target:
                return True
            elif matrix[Mr][Mc] < target:
                Lc = Mc + 1
            else:
                Rc = Mc - 1
        return False
