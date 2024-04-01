from collections import defaultdict
n = 6
meetings = [[1,2,5],[2,3,8],[1,5,10]]
firstPerson = 1
res=set([0,firstPerson])
time_stamp={}
for src,dst,t in meetings:
    if t not in time_stamp:
        time_stamp[t]=defaultdict(list)
    time_stamp[t][src].append(dst)    
    time_stamp[t][dst].append(src)
def dfs(src,adj):
    if src in visit:
        return
    visit.add(src)
    res.add(src)
    for nei in adj[src]:
        dfs(nei,adj)
    
    
for t in sorted(time_stamp.keys()):
    visit=set()
    for src in time_stamp[t]:
        if src in res:
            dfs(src,time_stamp[t])
return list(res)        
    
    
        