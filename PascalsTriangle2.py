# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascalTriangle = [ [1] * x for x in range(1,rowIndex+2)]        
        for row in range(2, len(pascalTriangle)):
            for col in range(1, row):
                pascalTriangle[row][col] = pascalTriangle[row-1][col] + pascalTriangle[row-1][col-1]
        return pascalTriangle[-1]