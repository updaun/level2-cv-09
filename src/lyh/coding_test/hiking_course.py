import heapq
graph = {}


def dijkstra(start, end, gates, summits):
    no_enter = gates[:] + summits[:]
    no_enter.remove(int(start))
    no_enter.remove(int(end))

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if current_destination == end:
            return distances[end]

        if distances[current_destination] < current_distance:
            continue
        
        if int(current_destination) in no_enter:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = max(current_distance, new_distance)
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances[end]


def fill_graph(n, paths):
    global graph

    for i in range(n):
        graph[str(i+1)] = dict()
    
    for path in paths:
        graph[str(path[0])][str(path[1])] = path[2]
        graph[str(path[1])][str(path[0])] = path[2]


def solution(n, paths, gates, summits):
    global graph
    fill_graph(n, paths)
    answer = []
    
    for gate in gates:
        for summit in summits:
            intensity = dijkstra(str(gate), str(summit), gates, summits)
            answer.append([summit, intensity])
    answer.sort(key = lambda x : (x[1], x[0]))
    return answer[0]