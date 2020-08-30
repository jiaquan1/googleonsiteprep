from collections import deque
def longestin2dmatrix(matrix):
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix)
    m = len(matrix[0])
    hmap = {}
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    q= deque()
    for i in range(n):
        for j in range(m):
            cnt = 0
            for dx,dy in directions:
                x = i+dx
                y = j+dy
                if 0<=x<n and 0<=y<m and matrix[x][y]<matrix[i][j]:
                    cnt +=1
            hmap[(i,j)] = cnt
            if cnt ==0:
                q.append((i,j))
    step = 0
    while q:
        size = len(q)
        newq = []
        for k in range(size):
            i,j = q.pop()
            for dx,dy in directions:
                x = i+dx
                y = j+dy
                if 0<=x<n and 0<=y<m and matrix[x][y]>matrix[i][j] and (x,y) in hmap:
                    hmap[(x,y)] -= 1
                    if hmap[(x,y)]==0:
                        newq.append((x,y))
        step +=1
        q = newq
    return step
matrix= [
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
print(longestin2dmatrix(matrix)) 


