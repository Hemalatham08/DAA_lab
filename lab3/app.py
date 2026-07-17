from flask import Flask, render_template
import heapq

app = Flask(__name__)

# ---------------- Union Find ----------------

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        return True


# ---------------- Kruskal ----------------

def kruskal(n, edges):

    edges.sort()

    uf = UnionFind(n)

    mst = []

    cost = 0

    for w, u, v in edges:

        if uf.union(u, v):

            mst.append((u, v, w))

            cost += w

            if len(mst) == n-1:
                break

    return mst, cost


# ---------------- Prim ----------------

def prim(n, adj):

    key = [float("inf")] * n

    parent = [-1] * n

    visited = [False] * n

    pq = [(0,0)]

    key[0] = 0

    mst = []

    cost = 0

    while pq:

        w,u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u]=True

        if parent[u]!=-1:

            mst.append((parent[u],u,w))

            cost += w

        for v,wt in adj.get(u,[]):

            if not visited[v] and wt<key[v]:

                key[v]=wt

                parent[v]=u

                heapq.heappush(pq,(wt,v))

    return mst,cost


@app.route("/")
def home():

    n = 7

    edges = [
        (7,0,1),
        (5,0,3),
        (8,1,2),
        (9,1,3),
        (7,1,4),
        (5,2,4),
        (15,3,4),
        (6,3,5),
        (8,4,5),
        (9,4,6),
        (11,5,6)
    ]

    adj={}

    for w,u,v in edges:

        adj.setdefault(u,[]).append((v,w))

        adj.setdefault(v,[]).append((u,w))

    k_mst,k_cost=kruskal(n,edges[:])

    p_mst,p_cost=prim(n,adj)

    return render_template(
        "index.html",
        k_mst=k_mst,
        k_cost=k_cost,
        p_mst=p_mst,
        p_cost=p_cost
    )


if __name__=="__main__":
    app.run(debug=True)