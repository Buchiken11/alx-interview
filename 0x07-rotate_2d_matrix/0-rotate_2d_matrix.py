#!/usr/bin/python3
"""
Rotating 2-D matrix
"""


def rotate_2d_matrix(m):
    """
    Rotates in-place
    """
    n = len(m)
    tmp1, tmp2 = 0, 0

    for j in range(0, len(m) // 2 + 1):
        for i in range(j, n - 1):
            # For r in first row, put in same position in col from back
            tmp1 = m[i][n - 1]
            m[i][n - 1] = m[j][i]
            # put that tmp1 in reverse position in row from bottom
            tmp2 = m[n - 1][n - 1 - i + j]
            m[n - 1][n - 1 - i + j] = tmp1
            # put that tmp2 in same position in col from front
            tmp1 = m[n - 1 - i + j][j]
            m[n - 1 - i + j][j] = tmp2
            # put that tmp1 in reverse position in row from top
            m[j][i] = tmp1
        n -= 1
