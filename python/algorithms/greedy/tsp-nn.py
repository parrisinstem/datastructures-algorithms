import math

def distance(city1, city2):
    # Function to calculate the Euclidean distance between two cities.
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tsp(cities):
    # Function to solve TSP using the Nearest Neighbor Algorithm.
    n = len(cities)
    visited = [False] * n
    tour = [0]  # Start the tour from the first city (assuming it's index 0).
    visited[0] = True

    for _ in range(n - 1):
        current_city = tour[-1]
        nearest_distance = float('inf')
        nearest_city = None

        for i in range(n):
            if not visited[i]:
                dist = distance(cities[current_city], cities[i])
                if dist < nearest_distance:
                    nearest_distance = dist
                    nearest_city = i

        tour.append(nearest_city)
        visited[nearest_city] = True

    return tour

# Example usage:
cities = [(0, 0), (1, 2), (3, 5), (2, 1), (5, 4), (4, 3)]
optimal_tour = nearest_neighbor_tsp(cities)
print("Optimal Tour:", optimal_tour)
