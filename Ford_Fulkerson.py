import time

def fordfulkerson(capacitymatrix, s, t):
    n = len(capacitymatrix)
    parent = [-1]*n
    maxflow = 0
    while True:
        if not breadthfirstsearch(capacitymatrix, s, t, parent):
            return maxflow
        pathflow = float("inf")
        w = t
        while(w != s):
            pathflow = min(pathflow, capacitymatrix[parent[w]][w])
            w = parent[w]
        maxflow += pathflow
        v = t
        while(v != s):
            u = parent[v]
            capacitymatrix[u][v] -= pathflow
            capacitymatrix[v][u] += pathflow
            v = parent[v]

def breadthfirstsearch(capacitymatrix, s, t, parent):
    n = len(capacitymatrix)
    visited = [False]*n
    queue = [s]
    visited[s] = True
    while len(queue) > 0:
        u = queue.pop(0)
        for i in range(n):
            if visited[i] == False and capacitymatrix[u][i] > 0:
                queue.append(i)
                visited[i] = True
                parent[i] = u
    return visited[t]

capacitymatrix = [[0, 8, 0, 0, 3, 0],
                 [0, 0, 9, 0, 0, 0],
                 [0, 0, 0, 0, 7, 2],
                 [0, 0, 0, 0, 0, 5],
                 [0, 0, 7, 4, 0, 0],
                 [0, 0, 0, 0, 0, 0]]

s = 0
t = 5

ti = time.time()
maxflow = fordfulkerson(capacitymatrix, s, t)
tf = time.time()

print("fordfulkerson :",maxflow,"\ntime :",tf-ti)
