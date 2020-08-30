def dragonandlakes(wea):
    res = []
    dictw={}
    dictw[0]=[]
    for day,w in enumerate(wea):
        if w!=0 and w not in dictw:
            dictw[w]=[day]
        elif w==0:
            dictw[0].append(day)
            res.append(0)
        else:
            if w in dictw and dictw[w]:
                if dictw[0]==[]:
                    return False
                elif dictw[0][-1]<dictw[w][0]:
                    return False
                elif dictw[0][-1]>dictw[w][0]:
                    res[-1]=w
                    dictw[0].remove(dictw[0][-1])
                    dictw[w]=[day]
    return res
wea = [1,2,0,2,3,0,1]
print(dragonandlakes(wea))

                



