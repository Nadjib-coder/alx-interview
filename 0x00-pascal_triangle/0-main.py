#!/usr/bin/python3
"""
This module contains the pascal_triangle function
that generates a specific number of rows of Pascal's triangle.
"""

def pascal_triangle(n):
    if n <= 0:  # Adjusted this to handle n = 0 case too
        return []
    
    triangle = []
    
    for i in range(n):
        # Start the row with all 1's
        row = [1] * (i + 1)
    
        # Fill in the middle elements of the row (if i > 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    
        # Append the completed row to the triangle
        triangle.append(row)
    
    return triangle
