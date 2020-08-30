def mergelabels( labels):
    Open, Close = 0,1
    events = []
    for label in labels:
        events.append((label[0],Open,label[2]))
        events.append((label[1],Close,label[2]))
    events.sort()
    res = []
    seen = set()
    prevstart = float('inf')
    for time,eventtype,label in events:
        if prevstart is not time:
            if seen:
                res.append((prevstart,time,sorted(seen)))
            prevstart = time
        if eventtype == Open:
            seen.add(label)
        else:
            seen.remove(label)
    return res
labelS = [[0,3,'A'],[2,4,'B'],[5,6,'C']]
print(mergelabels(labelS))