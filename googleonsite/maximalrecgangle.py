class Solution:
    def maximalRectangle(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        height = [0]*cols
        area = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]=='0':
                    height[col]=0
                elif matrix[row][col]=='1':
                    height[col] += 1
            area = max(area,self.getarea(height))
            #print(height)
        return area
    def getarea(self,height):
        height.append(0)
        n = len(height)
        stack = [-1]
        area = 0
        for i in range(n):
            
            while height[i]<height[stack[-1]]:
                h = height[stack.pop()]
                w = i-stack[-1]-1
                #print(i,h,w)
                area = max(area,h*w)
            stack.append(i)
        height.pop()
        return area
a = Solution()
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print(a.maximalRectangle(matrix))