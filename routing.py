import heapq
from graph import graph

def shortest_path(start, end):
    pq = [(0, start)]
    parent = {}
    cost_map = {start: 0}

    while pq:
        cost, node = heapq.heappop(pq)

        if node == end:
            break

        for neighbor, weight in graph[node].items():
            new_cost = cost + weight

            if neighbor not in cost_map or new_cost < cost_map[neighbor]:
                cost_map[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(pq, (new_cost, neighbor))

    # reconstruct path
    path = []
    curr = end

    while curr in parent:
        path.append(curr)
        curr = parent[curr]

    path.append(start)
    path.reverse()

    return cost_map.get(end, float("inf")), path