#!/usr/bin/python3
"""
module to compute the permeter of an island
"""


def island_perimeter(grid):
    """
    Computing the perimeter of an island without lakes.
    """
    island_perimeter = 0
    if type(grid) != list:
        return None
    n = len(grid)
    for i, row in enumerate(grid):
        p = len(row)
        for j, cell_peri in enumerate(row):
            if cell_peri == 0:
                continue
            perimeter_edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == p - 1 or (p > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            island_perimeter += sum(perimeter_edges)
    return island_perimeter
