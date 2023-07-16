# Importing necessary functions from heapq and inf constant from math
from heapq import heappop, heappush
from math import inf

# The graph represented using a dictionary where each vertex maps to a list of its neighbors and edge weights
graph = {
    'A': [('B', 10), ('C', 3)],
    'C': [('D', 2)],
    'D': [('E', 10)],
    'E': [('A', 7)],
    'B': [('C', 3), ('D', 2)]
}


# Function to calculate the shortest distances from the given start vertex to all other vertices using Dijkstra's algorithm
def dijkstras(graph, start):
    distances = {}

    # Initializing distances dictionary with infinity for all vertices
    for vertex in graph:
        distances[vertex] = inf

    # Distance from start to start vertex is set to 0
    distances[start] = 0

    # List to store vertices and their respective distances as tuples (distance, vertex)
    # Using a heap to maintain the list with minimum distance at the top
    vertices_to_explore = [(0, start)]

    # Main loop to explore vertices and update distances
    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)  # Getting the vertex with the smallest distance

        # Exploring neighbors of the current vertex
        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight  # Calculate the new distance from the start vertex

            # If the new distance is smaller than the current distance recorded, update the distances dictionary
            # and add the neighbor vertex with the new distance to the heap for further exploration
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))

    # Return the final distances dictionary containing the shortest distances from the start vertex
    return distances


# Applying Dijkstra's algorithm to find the shortest distances from vertex 'D' to all other vertices
distances_from_d = dijkstras(graph, 'A')

# Printing the result
print("\n\nShortest Distances: {0}".format(distances_from_d))
