class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows
        currentRow = set()
        for i in range(9):
            currentRow = set()
            for j in range(9):
                if board[i][j] in currentRow:
                    return False
                elif board[i][j] != '.':
                    currentRow.add(board[i][j])

        # check cols 
        currentCol = set()
        for i in range(9):
            currentCol = set()
            for j in range(9):
                if board[j][i] in currentCol:
                    return False
                elif board[j][i] != '.':
                    currentCol.add(board[j][i])

        # check blocks
        # 9 blocks, each 3x3 
        for i in range(3):
            for j in range(3):
                # per block code 
                currentBlock = set()
                for x in range(3*i,3*i + 3):
                    for y in range(3*j, 3*j + 3):
                        if board[x][y] in currentBlock:
                            return False
                        elif board[x][y] != '.':
                            currentBlock.add(board[x][y])


        return True