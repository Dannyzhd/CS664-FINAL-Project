# implimentation with an actual graph.

graph = {
    "Boston": {
    	"Manchester": {"Car":{"cost":47, "time":73}, "Plane":{"cost":273, "time":426}}, 
    	"Franconia": {"Car":{"cost":60.5, "time":152}, "Plane":{"cost":999, "time":999}},
    	"Jay": {"Car":{"cost":72, "time":235}, "Plane":{"cost": 999, "time": 999}},
    	"Stowe": {"Car":{"cost":68, "time":204}, "Plane":{"cost":999, "time":999}},
    	"Albany": {"Car":{"cost":64, "time":183}, "Plane":{"cost":256, "time":221}},
    	"Pisgah": {"Car":{"cost":78, "time":326}, "Plane":{"cost":999, "time":999}}
    	},
    "Manchester": {
    	"Boston": {"Car":{"cost":47, "time":73}, "Plane":{"cost":273, "time":426}},
    	"Franconia": {"Car":{"cost":53, "time":88}, "Plane":{"cost":999, "time":999}},
    	"Jay": {"Car":{"cost":65, "time":232}, "Plane":{"cost":999, "time":999}},
    	"Stowe": {"Car":{"cost":61, "time":140}, "Plane":{"cost":999, "time":999}},
    	"Albany": {"Car":{"cost":63, "time":201}, "Plane":{"cost":291, "time":222}},
    	"Pisgah": {"Car":{"cost":70, "time":258}, "Plane":{"cost":999, "time":999}}
    	},
    "Franconia": {
    	"Boston": {"Car":{"cost":60.5, "time":152}, "Plane":{"cost":999, "time":999}},
    	"Manchester": {"Car":{"cost":53, "time":88}, "Plane":{"cost":999, "time":999}},
    	"Jay": {"Car":{"cost":52, "time":81}, "Plane":{"cost":999, "time":999}},
    	"Stowe": {"Car":{"cost":50, "time":85}, "Plane":{"cost":999, "time":999}},
    	"Albany": {"Car":{"cost":67, "time":224}, "Plane":{"cost":999, "time":999}},
    	"Pisgah": {"Car":{"cost":65, "time":228}, "Plane":{"cost":999, "time":999}}
    	},
    "Jay": {
    	"Boston": {"Car":{"cost":72, "time":235}, "Plane":{"cost":999, "time":999}},
    	"Manchester": {"Car":{"cost":65, "time":232}, "Plane":{"cost":999, "time":999}},
    	"Franconia": {"Car":{"cost":52, "time":81}, "Plane":{"cost":999, "time":999}},
    	"Stowe": {"Car":{"cost":46, "time":55}, "Plane":{"cost":999, "time":999}},
    	"Albany": {"Car":{"cost":74, "time":256}, "Plane":{"cost":999, "time":999}},
    	"Pisgah": {"Car":{"cost":58, "time":164}, "Plane":{"cost":999, "time":999}}
    	},
    "Stowe": {
    	"Boston": {"Car":{"cost":68, "time":204}, "Plane":{"cost":999, "time":999}},
    	"Manchester": {"Car":{"cost":61, "time":140}, "Plane":{"cost":999, "time":999}},
    	"Franconia": {"Car":{"cost":50, "time":85}, "Plane":{"cost":999, "time":999}},
    	"Jay": {"Car":{"cost":46, "time":55}, "Plane":{"cost":999, "time":999}},
    	"Albany": {"Car":{"cost":65, "time":209}, "Plane":{"cost":999, "time":999}},
    	"Pisgah": {"Car":{"cost":56, "time":160}, "Plane":{"cost":999, "time":999}}
    	},
    "Albany": {
    	"Boston": {"Car":{"cost":64, "time":183}, "Plane":{"cost":256, "time":221}},
    	"Manchester": {"Car":{"cost":63, "time":201}, "Plane":{"cost":291, "time":222}},
    	"Franconia": {"Car":{"cost":67, "time":224}, "Plane":{"cost":999, "time":999}},
    	"Jay": {"Car":{"cost":74, "time":256}, "Plane":{"cost":999, "time":999}},
    	"Stowe": {"Car":{"cost":65, "time":209}, "Plane":{"cost":999, "time":999}},
    	"Pisgah": {"Car":{"cost":61, "time":154}, "Plane":{"cost":999, "time":999}}
    	},
    "Pisgah": {
    	"Boston": {"Car":{"cost":78, "time":326}, "Plane":{"cost":999, "time":999}},
    	"Manchester": {"Car":{"cost":70, "time":258}, "Plane":{"cost":999, "time":999}},
    	"Franconia": {"Car":{"cost":65, "time":228}, "Plane":{"cost":999, "time":999}},
    	"Jay": {"Car":{"cost":58, "time":164}, "Plane":{"cost":999, "time":999}},
    	"Stowe": {"Car":{"cost":56, "time":160}, "Plane":{"cost":999, "time":999}},
    	"Albany": {"Car":{"cost":61, "time":154}, "Plane":{"cost":999, "time":999}}
    	}
    }

Trans_method = ['Car', 'Plane']

# path1 = ['A', 'B', 'C', 'E', 'D', 'F']


# (plane:(cost time) car:(cost time))


source = "Boston"
destination = "Jay"
initial_path = []
transportations = []
trans_initial = []
visited = []
paths = []
constraint_value_cost = 200
constraint_value_time = 500

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

ind






