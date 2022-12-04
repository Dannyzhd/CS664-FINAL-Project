import sys

'''in order to form infinity'''
from heapq import heapify, heappush, heappop

'''to use when finding the neighbor of a vertex with the minimum cost
using heap functions has lower time complexity than sorting'''

''' Three inputs: 1. graph: graph in the form of dictionary, 2. src: standing for source, the
beginning vertex, 3. dest: the destination.'''


def dijkstra(graph, src, dest):
    # define infinity
    inf = sys.maxsize

    # define dictionary node_data: recording the cost and predecessor of each node.
    # initial cost of each node is infinity
    # pred will record the path from source to that node.
    node_data = {'A': {'cost': inf, 'pred': []},
                 'B': {'cost': inf, 'pred': []},
                 'C': {'cost': inf, 'pred': []},
                 'D': {'cost': inf, 'pred': []},
                 'E': {'cost': inf, 'pred': []},
                 'F': {'cost': inf, 'pred': []}
                 }

    # now for source node we assign it to be zero as a beginning.
    node_data[src]["cost"] = 0

    # create a list to record visited vertices.
    visited = []

    # current location to record current location, upon which we find the min cost neighbor.
    # initially it is the source vertex.
    current = src

    # create a for loop of length n-1, where n is the number of vertices.
    for i in range(len(node_data) - 1):

        # find out whether or not the current position is visited
        # if it is not, push it into the "visited" list. Since we are now visiting it.
        if current not in visited:
            visited.append(current)
            # an empty set min_heap
            min_heap = []
            # a for loop to check through the neighbors of the current vertex.
            # to find out which of the neighbor has minimum cost.
            for j in graph[current]:
                # if the neighbor is already visited we no longer evaluate it.
                if j not in visited:
                    # the new cost for the neighbor to evaluate is then:
                    # cost(current position) + edge_length(current position, the neighbor)
                    cost = node_data[current]["cost"] + graph[current][j]
                    # now we compare the cost with original cost assigned to that neighbor
                    # if the new cost is lower, we re-assign it to the cost of that neighbor.
                    if cost < node_data[j]['cost']:
                        # for example in the beginning when we visit current = A then in this loop B and C will
                        # respectively be assigned lengths of edge AB, AC as their new costs in replacement of the
                        # original infinity.
                        node_data[j]['cost'] = cost
                        # when this condition holds, we record the current position to predecessor of that neighbor
                        # as one step of the path. the path = (ordered list of previous vertices before current
                        # vertex) + (current vertex)
                        node_data[j]["pred"] = node_data[current]['pred'] + list(current)
                    # for each of the neighbor, record the cost and its name into the heap as a tuple.
                    heappush(min_heap, (node_data[j]["cost"], j))
                    print(min_heap)
                # to find the minimum element we heapify the min_heap
        heapify(min_heap)
        # re-define current stage to be the vertex with the minimum cost.
        # [0] give us the minimum tuple [1] then index the vertex name corresponding to it.
        current = min_heap[0][1]

    # print the shortest distance and the corresponding path.
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]["pred"] + list(dest)))


if __name__ == "__main__":
    graph = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "C": 3, "D": 8},
    "C": {"A": 4, "B": 3, "E": 5, "D": 2},
    "D": {"B": 8, "C": 2, "E": 11, "F": 22},
    "E": {"C": 5, "D": 11, "F": 1},
    "F": {"D": 22, "E": 1}
    }
    source = 'A'
    destination = "F"
    dijkstra(graph, source, destination)