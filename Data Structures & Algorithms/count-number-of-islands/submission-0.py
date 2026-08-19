class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if len(grid[0]) == 0:
            return 0

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        dq = deque()

        numberOfIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                elif grid[i][j] == '1':
                    # mark visited i.e. turn 0
                    # insert in queue 
                    # start expanding
                    grid[i][j] = '0'
                    dq.append((i,j))
                    while dq:
                        currRow, currCol = dq.popleft()

                        for x,y in directions: 
                            newRow, newCol = int(currRow) + x, int(currCol) + y
                            if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]):
                                if grid[newRow][newCol] == '1':
                                    grid[newRow][newCol] = '0'
                                    dq.append((newRow,newCol))

                    numberOfIslands += 1


        return numberOfIslands
        