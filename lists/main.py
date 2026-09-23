buggy_grid = [[0] * 3] * 3
buggy_grid[0][0] = 99
print("Buggy grid (all rows changed):", buggy_grid)

safe_grid = [[0 for _ in range(3)] for _ in range(3)]
safe_grid[0][0] = 99
print("Safe grid (only first row changed):", safe_grid)
