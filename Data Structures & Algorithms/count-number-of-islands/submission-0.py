class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x,y):
            if grid[x][y] == "0":
                return 

            grid[x][y] = "0"

            if x + 1 < len(grid):
                dfs(x+1,y)
            if x - 1 >= 0:
                dfs(x-1,y)
            if y + 1 < len(grid[0]):
                dfs(x,y+1)
            if y - 1 >= 0:
                dfs(x,y-1)


        numIslands = 0 
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    print(x)
                    print(y)
                    numIslands += 1
                    dfs(x,y)
        
        return numIslands


        