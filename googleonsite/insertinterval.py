def insert(intervals, newInterval):
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        res=[]
        i=0
        newstart, newend = newInterval[0],newInterval[1]
        while i<n and newstart > intervals[i][0]:
            res.append(intervals[i])
            i+=1
        if not res or res[-1][1]<newstart:
            res.append(newInterval)
        else:
            res[-1][1]=max(res[-1][1],newend)
        while i<n:
            start, end = intervals[i][0],intervals[i][1]
            i+=1
            if res[-1][1]<start:
                res.append([start,end])
            else:
                res[-1][1] = max(res[-1][1],end) 
        return res
intervals=[[1,5]]
newInterval=[2,3]
print(insert(intervals,newInterval))