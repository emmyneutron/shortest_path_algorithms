"""
Name: Zaman
Course: IEM 5063
Course_Professor: Dr. Baski
"""

def  bellman_ford(Graph, nLine, source):
    import time
    import numpy as np
    import pandas as pd
    
    file1 = Graph
    X = np.genfromtxt(file1, comments = 'c')
    X = X[:nLine]
    l = len(X) - 1

    #adjacency list start from here
    vlist = []
    weightlist = []
    maxwt = 0
    for i in range(1,l):
        vlist.append(X[i,1])
        weightlist.append((X[i,1],X[i,2]))
        
    vdict = dict.fromkeys(vlist)
    wdict = dict.fromkeys(weightlist)
    
    for i in range(1,l):
        vdict[X[i,1]] = []
        wdict[(X[i,1],X[i,2])] = X[i,3]
        
    for i in range(1,l):
        vdict[X[i,1]].append(X[i,2])
        if maxwt <= X[i,3]:
            maxwt = X[i,3]
    #END
    
    #INTIALIZE-SINGLE-SOURCE(G, s)
    n = len(vdict.keys())
    source = source
    dist = {}
    pred= {}
    for key in vdict:
        dist[key] = maxwt*n
        pred[key] = -1
    dist[source] = 0
    pred[source] = 0
    Q = [source]
    #END
    

    #Algorithm start here
    start = time. time()
    
    while Q != []:
        u = Q[0]
        Q.pop(0)
        for v in vdict[u]:
            if dist[v] > dist[u] + wdict[u,v]:
                dist[v] = dist[u] + wdict[u,v]
                pred[v] = u
                if v not in Q:
                    Q.append(v)
    
    #Algorithm end here


    #printing end here
    end = time. time()
    print(lines, ' : ' ,end - start)
    

    df = np.zeros((n, 3))
    i = 0
    for key in vdict:
        a = key
        b = dist[a]
        c = pred[a]
        df[i] = [a, b, c]
        i = i+1
    
    dataset = pd.DataFrame({'Distination' : df[:,0], 'Distance' : df[:,1],'NodesBetween' : df[:,2]})
    dataset.to_csv('output'+ str(nLine)+'.csv' , sep = '\t', index =False)
    #code end here
    
if __name__ == "__main__":
	Line_list=[64, 128, 256, 512, 1024, 2048, 4096]
	for n in Line_list:
		bellman_ford('USA-road-d.NY.gr', n, 1)
		print('______________________________')



