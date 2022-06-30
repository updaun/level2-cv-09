graph = {
	1: [2,3,4],
	2:[5],
	3:[5],
	4:[],
	5:[6,7],
	6:[],
	7:[3],
}

def iterative_bfs(start_vertex):
    visited = [start_vertex]
    queue = [start_vertex]
    while queue:
        vertex = queue.pop(0)
        for item in graph[vertex]:
            if item not in visited:
                visited.append(item)
                queue.append(item)
    return visited

print(iterative_bfs(1))