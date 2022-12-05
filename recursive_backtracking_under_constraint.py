# Here we want to find all paths and their corresponding cost by recursively searching.


graph = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "C": 3, "D": 8},
    "C": {"A": 4, "B": 3, "E": 5, "D": 2},
    "D": {"B": 8, "C": 2, "E": 11, "F": 22},
    "E": {"C": 5, "D": 11, "F": 1},
    "F": {"D": 22, "E": 1}
    }



# path1 = ['A', 'B', 'C', 'E', 'D', 'F']




source = "A"
destination = "E"
path = []
visited = []
paths = []
constraint_value = 15

## This function returns all paths from beparture to destination such that the summed cost is below or equal to the budget.
def get_all_paths_under_constraint(gra, src, des, pat, vis):
    vis.append(src)
    pat.append(src)
    if count_path_weight(pat) > constraint_value:  # check if it is consistent
        return
    elif src == des:
        paths.append(pat)
        return
    else:
        for i in gra[src]:
            if i not in vis:
                get_all_paths_under_constraint(gra, i, des, pat.copy(), vis.copy())


get_all_paths_under_constraint(graph, source, destination, path, visited)



def count_path_weight(p):
    total = 0
    for i in range(len(p)-1):
        total += graph[p[i]][p[i+1]]
    return total



paths_weights = dict([])
for j in paths:
    paths_weights[str(j)] = count_path_weight(j)
paths_weights


