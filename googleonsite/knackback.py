def knackback1(n,v,goods):
    dp = [[0 for _ in range(v+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,v+1):
            dp[i][j]=dp[i-1][j]
            if j >=goods[i-1][0]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-goods[i-1][0]]+goods[i-1][1])
    print(dp[-1][-1])
def knackback2(n,v,goods):
    dp = [0 for _ in range(v+1)]
    for i in range(n):
        for j in range(v,-1,-1):
            
            if j >=goods[i][0]:
                dp[j] = max(dp[j], dp[j-goods[i][0]]+goods[i][1])
    print(dp[-1])
def knackback3(n,v,vols,weight):
    dp = [0 for _ in range(v+1)]
    for i,vol in enumerate(vols):
        for x in range(vol,v+1):
            dp[x]=max(dp[x],dp[x-vol]+weight[i])
    print(dp[-1])


n = 5
v = 10
goods = [[1,3],[3,5],[7,1],[5,20],[6,10]]
vols = [1,3,7,5,6]
weight = [3,5,1,20,10]
# knackback1(n,v,goods)
# knackback2(n,v,goods)
knackback3(n,v,vols,weight)


