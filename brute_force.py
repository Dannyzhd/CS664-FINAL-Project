# Here we want to find all paths and their corresponding cost by recursively searching.


graph = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "C": 3, "D": 8},
    "C": {"A": 4, "B": 3, "E": 5, "D": 2},
    "D": {"B": 8, "C": 2, "E": 11, "F": 22},
    "E": {"C": 5, "D": 11, "F": 1},
    "F": {"D": 22, "E": 1}
    }


src = "A"
dest = "F"
path = []
visited = []
paths = []


def get_all_paths(graph, src, dest, path, visited, paths):
    beginning = src
    visited.append(src)
    path.append(src)

    if src == dest:
        paths.append(path)
        # remove everything from visited to start a new search.
        path = [beginning]
        visited = [beginning]
        print(paths)
    else:
        for i in graph[src]:
            if i not in visited:
                get_all_paths(graph, i, dest, path, visited, paths)


get_all_paths(graph, "A", "F", path, visited, paths)


# def get_all_paths(graph, src, dest):
#     path.append(src)
#     visited.append(src)
#     # if current vertex is already the destination simply return the path.
#     if src == dest:
#         path += list(dest)
#         paths.append(path)
#     else:
#         for i in graph['src']:
#             if i not in visited




