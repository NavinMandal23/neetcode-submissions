class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r, c = len(board), len(board[0])

        rows = {r1 : set() for r1 in range(r)} 
        cols = {c1 : set() for c1 in range(c)}
        squares = {(r2//3, c2//3) : set() for r2 in range(r) for c2 in range(c)}

        for i in range(r):
            for j in range(c):
                num = board[i][j]
                if num == '.':
                    continue
                if num in rows[i] or num in cols[j] or num in squares[(i//3, j//3)]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                squares[(i//3, j//3)].add(num)
                
        return True
                
