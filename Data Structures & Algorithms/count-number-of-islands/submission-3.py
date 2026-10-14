class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # iterate over all elements - O n2 
        # if you find a 0 skip/continue
        # if you find a (unvisited) 1 - it's the start of an island
        # start your bfs 
        # put 1 in the queue 
        # check all 4 directions next to it (make sure directions are valid!)
        # if any of them is a 1, put that in q 
        # continue expanding until your q is empty 
        # when q becomes empty - increment no of islands

        # if we visit a 1 - change it into 0 so we don't visit it again 

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        directions = [(-1,0), (1,0), (0,-1), (0,1)]


        # ["0","0","0","0","1"],
        # ["0","1","0","0","1"],

        # q 1,0 0,1
        for i in range(rows):
            for j in range(cols): 
                if grid[i][j] == '0':
                    continue
                q = deque()
                q.append((i,j))
                grid[i][j] = '0'
                while q:
                    r,c = q.pop()

                    for d in directions:
                        next_r, next_c = r + d[0], c + d[1]
                        if 0 <= next_r < rows and 0 <= next_c < cols:
                            if grid[next_r][next_c] == '1':
                                q.append((next_r, next_c))
                                grid[next_r][next_c] = '0'
                islands += 1 


        return islands




















        # if len(grid[0]) == 0:
        #     return 0

        # directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # dq = deque()

        # numberOfIslands = 0

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == '0':
        #             continue
        #         elif grid[i][j] == '1':
        #             # mark visited i.e. turn 0
        #             # insert in queue 
        #             # start expanding
        #             grid[i][j] = '0'
        #             dq.append((i,j))
        #             while dq:
        #                 currRow, currCol = dq.popleft()

        #                 for x,y in directions: 
        #                     newRow, newCol = int(currRow) + x, int(currCol) + y
        #                     if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]):
        #                         if grid[newRow][newCol] == '1':
        #                             grid[newRow][newCol] = '0'
        #                             dq.append((newRow,newCol))

        #             numberOfIslands += 1


        # return numberOfIslands
        