# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]

#Dynamic Method
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = [ [1] * x for x in range(1,numRows+1)]        
        for row in range(2, len(pascalTriangle)):
            for col in range(1, row):
                pascalTriangle[row][col] = pascalTriangle[row-1][col] + pascalTriangle[row-1][col-1]
        return pascalTriangle


#Basic Method
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = []
        for i in range(numRows):
            if i==0:
                l.append([1])
            else:
                x = [1]
                j = 1
                while j<i:
                    x.append(l[-1][j-1]+l[-1][j])
                    j=j+1
                x.append(1)
                l.append(x)
        return l