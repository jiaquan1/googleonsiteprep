def isIsomorphic(s, t):
    # if two strings have different length, not isomorphic
    if len(s) != len(t):    
        return False
    n = len(s)
    #store the index of each characters in a dict,key is character, value is indexs,
    #matched characters should have same indexs in two strings
    sres = {}
    tres = {}
    for i,x in enumerate(s):
        sres[x]=sres.get(x,[])+[i]
    for i,x in enumerate(t):
        tres[x]=tres.get(x,[])+[i]
    #print(sorted(sres.values()),sorted(tres.values()))
    return sorted(sres.values())==sorted(tres.values())   
s1 = 'egg'
t1 = 'add'
s2 = 'foo'
t2 = 'bar'
s3 = 'paper'
t3 = 'title'
print(isIsomorphic(s1,t1), isIsomorphic(s2,t2),isIsomorphic(s3,t3))