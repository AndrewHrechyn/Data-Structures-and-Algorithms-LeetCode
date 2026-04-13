def dfs(i, j, grid):

    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
        return
    
    grid[i][j] = '0'

    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)

def main():
    n, m = map(int, input().split())

    grid = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        row = input().strip()
        for j in range(m):
            grid[i][j] = row[j]

    count = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)

    print(count)