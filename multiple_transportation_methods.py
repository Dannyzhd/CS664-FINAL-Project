# Here we want to find all paths and their corresponding cost and time by recursively searching
# such that neither time and cost are surpassed.
from heapq import heapify

graph = {
    "A": {"B": {"Train": {"cost": 2, "time": 10}, "Plane": {"cost": 15, "time": 1}},
          "C": {"Train": {"cost": 3, "time": 15}, "Plane": {"cost": 28, "time": 2}}},
    "B": {"A": {"Train": {"cost": 2, "time": 10}, "Plane": {"cost": 15, "time": 3}},
          "C": {"Train": {"cost": 6, "time": 30}, "Plane": {"cost": 40, "time": 2}},
          "D": {"Train": {"cost": 3, "time": 15}, "Plane": {"cost": 75, "time": 4}}},
    "C": {"A": {"Train": {"cost": 3, "time": 15}, "Plane": {"cost": 28, "time": 2}},
          "B": {"Train": {"cost": 6, "time": 30}, "Plane": {"cost": 40, "time": 4}},
          "E": {"Train": {"cost": 5, "time": 10}, "Plane": {"cost": 100, "time": 1}},
          "D": {"Train": {"cost": 2, "time": 10}, "Plane": {"cost": 78, "time": 3}}},
    "D": {"B": {"Train": {"cost": 8, "time": 10}, "Plane": {"cost": 55, "time": 5}},
          "C": {"Train": {"cost": 2, "time": 10}, "Plane": {"cost": 40, "time": 1}},
          "E": {"Train": {"cost": 11, "time": 10}, "Plane": {"cost": 98, "time": 2}},
          "F": {"Train": {"cost": 22, "time": 10}, "Plane": {"cost": 76, "time": 7}}},
    "E": {"C": {"Train": {"cost": 5, "time": 10}, "Plane": {"cost": 80, "time": 4}},
          "D": {"Train": {"cost": 11, "time": 10}, "Plane": {"cost": 70, "time": 2}},
          "F": {"Train": {"cost": 1, "time": 10}, "Plane": {"cost": 77, "time": 1}}},
    "F": {"D": {"Train": {"cost": 22, "time": 10}, "Plane": {"cost": 100, "time": 2}},
          "E": {"Train": {"cost": 1, "time": 10}, "Plane": {"cost": 122, "time": 3}}}
}

Trans_method = ['Plane', 'Train']

# path1 = ['A', 'B', 'C', 'E', 'D', 'F']


# (plane:(cost time) car:(cost time))


source = "A"
destination = "E"
initial_path = []
transportations = []
trans_initial = []
visited = []
paths = []
constraint_value_cost = 150
constraint_value_time = 20

# two functions to help count total summed cost and time respectively.
path1 = ["A", 'B', 'C']


def count_path_total_cost(path, transit_mode):
    total = 0
    for i in range(len(path) - 1):
        total += graph[path[i]][path[i + 1]][transit_mode[i]]["cost"]
    return total


# demo for counting methods:
# path1 = ['A', 'B', 'C']
# trans1 = ['Plane', 'Train']
# count_path_total_cost(path1, trans1)
# count_path_total_time(path1, trans1)

def count_path_total_time(path, transit_mode):
    total = 0
    for i in range(len(path) - 1):
        total += graph[path[i]][path[i + 1]][transit_mode[i]]["time"]
    return total


## This function returns all paths from departure to destination such that the summed cost is below or equal to the budget.
def get_all_paths_under_constraint(gra, src, des, path, vis, trans, transit_mode=""):
    vis.append(src)
    path.append(src)
    # skip adding transit mode for starting node
    if transit_mode != "":
        trans.append(transit_mode)
    if (count_path_total_cost(path, trans) > constraint_value_cost) or (
            count_path_total_time(path, trans) > constraint_value_time):  # check if it is consistent
        return
    elif src == des:
        paths.append((path, trans))
        return
    else:
        for i in gra[src]:
            if i not in vis:
                for mode in Trans_method:
                    get_all_paths_under_constraint(gra, i, des, path.copy(), vis.copy(), trans.copy(), mode)


get_all_paths_under_constraint(graph, source, destination, initial_path, visited, trans_initial)
print(paths)

paths_cost = dict([])
paths_time = dict([])
for j in paths:
    paths_time[str(j)] = count_path_total_time(j[0], j[1])

for j in paths:
    paths_cost[str(j)] = count_path_total_cost(j[0], j[1])
    # paths_cost[str(j)] = count_path_total_cost(j)
paths_cost
paths_time

ind = sorted(paths_cost, key = paths_cost.get)


# this sort the cost ascendingly.
ind = sorted(paths_cost.items(), key = lambda x: x[1])

paths_cost[]






