import heapq
def conflictrooms(calendar,rooms,queries):
    res = [True for _ in range(len(queries))]
    calendar.sort(key = lambda x: x[0])
    for i, query in enumerate(queries):
        intervals = []
        intervals.append(query)
        for block in calendar:
            if block[1]<=query[0]:
                continue
            elif block[0]>=query[1]:
                break
            else:
                intervals.append(block)
        intervals.sort(key = lambda x: x[0])
        prevend = intervals[0][1]
        rm = []
        heapq.heappush(rm,prevend)
        for interval in intervals[1:]:
            if interval[0]<rm[0]:
                heapq.heappush(rm,interval[1])
            else:
                heapq.heappop(rm)
                heapq.heappush(rm,interval[1])
            if len(rm)>rooms:
                res[i]=False
    return res
#print(conflictrooms([[1, 2], [4, 5], [8, 10]],1,[[2, 3], [3, 4]]))
print(conflictrooms([[1, 3], [4, 6], [6, 8], [9, 11], [6, 9], [1, 3], [4, 10]],3,[[1, 9], [2, 6], [7, 9], [3, 5], [3, 9], [2, 4], [7, 10], [5, 9], [3, 10], [9, 10]]))


    

