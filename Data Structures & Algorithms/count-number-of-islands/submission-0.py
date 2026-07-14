class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    self.dfs(r, c, grid, ROWS, COLS)
                    islands += 1
        return islands
    
    def dfs(self, r, c, grid, ROWS, COLS):
        # defining 4 directions possibility to go
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # base class
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
            return
        
        # If found land --> "1"

        grid[r][c] = "0" # mark it visited

        for dr, dc in directions:
            self.dfs(r+dr, c+dc, grid, ROWS, COLS)

        