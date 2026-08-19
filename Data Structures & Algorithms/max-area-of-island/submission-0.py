class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid[0]) == 0:
            return 0

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        dq = deque()

        numberOfIslands = 0
        maxIslandSize = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                elif grid[i][j] == 1:

                    # mark visited i.e. turn 0
                    # insert in queue 
                    # start expanding
                    grid[i][j] = 0
                    dq.append((i,j))
                    currentIslandSize = 0
                    while dq:
                        currRow, currCol = dq.popleft()
                        currentIslandSize += 1
                        for x,y in directions: 
                            newRow, newCol = currRow + x, currCol + y
                            if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]):
                                if grid[newRow][newCol] == 1:
                                    grid[newRow][newCol] = 0
                                    dq.append((newRow,newCol))
                    maxIslandSize = max(currentIslandSize,maxIslandSize)
                    # numberOfIslands += 1


        return maxIslandSize