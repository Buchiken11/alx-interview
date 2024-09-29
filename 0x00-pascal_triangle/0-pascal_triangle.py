#!/usr/bin/python3
'''
A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''
    Creates a list of lists of integers representing
    the Pascal's triangle of a given n integer.
    '''
    p_triangle = []
    if type(n) is not int or n <= 0:
        return p_triangle
    for i in range(n):
        line = []
        for p in range(i + 1):
            if p == 0 or p == i:
                line.append(1)
            elif i > 0 and p > 0:
                line.append(p_triangle[i - 1][p - 1] + p_triangle[i - 1][p])
        p_triangle.append(line)
    return p_triangle
