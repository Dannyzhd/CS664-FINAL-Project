class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def find_path_near_budget(self, src, destination, budget):
        # Create a path array with nothing included
        # in path
        path = [False]*self.V

        # Add source vertex to path
        path[src] = 1

        return self.path_more_than_budget(src, destination, budget, path)

    # Prints shortest paths from src to all other vertices
    def path_more_than_budget(self, src, destination, budget, path):
        # If budget is 0 or negative, return true
        if budget <= 0:
            return True

        # Get all adjacent vertices of source vertex src and
        # recursively explore all paths from src.
        i = 0
        while i != len(self.adj[src]):
            # Get adjacent vertex and weight of edge
            v = self.adj[src][i][0]
            w = self.adj[src][i][1]
            i += 1

            # If v is already in path, ignore
            if path[v]:
                continue

            # If weight of is more than k, return true
            if w >= budget:
                return True

            # Else add this vertex to path
            path[v] = True

            # If this adjacent can provide a path longer
            # than k, return true.
            if self.path_more_than_budget(v, destination, budget - w, path):
                return True

            # Backtrack
            path[v] = False

        # If no adjacent could produce longer path, return
        # false
        return False

    # Utility function to an edge (u, v) of weight w
    def add_edge(self, u, v, w):
        self.adj[u].append([v, w])
        self.adj[v].append([u, w])

if __name__ == "__main__":

    V = 6
    g = Graph(V)

    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5

    g.add_edge(a, 1, 2)
    g.add_edge(a, 2, 4)
    g.add_edge(b, 2, 3)
    g.add_edge(b, 3, 8)
    g.add_edge(c, 3, 2)
    g.add_edge(c, 4, 5)
    g.add_edge(d, 4, 11)
    g.add_edge(d, 5, 22)
    g.add_edge(e, 5, 1)


    source = 0
    dest = 5
    cost = 42
    if g.find_path_near_budget(source, dest, cost):
        print("true")
    else:
        print("false")