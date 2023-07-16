import heapq

def a_star(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Helper function to calculate the heuristic (Manhattan distance)
    def heuristic(node):
        return abs(node[0] - end[0]) + abs(node[1] - end[1])

    # Priority queue for the open set, containing nodes to explore
    open_set = [(0, start)]
    # Set to keep track of visited cells
    visited = set()
    # Dictionary to store parent cells for backtracking the path
    parent = {}

    while open_set:
        cost, current = heapq.heappop(open_set)
        visited.add(current)

        if current == end:
            # Reconstruct the path from end to start using parent dictionary
            path = []
            while current in parent:
                path.insert(0, current)
                current = parent[current]
            path.insert(0, start)
            return path

        for dx, dy in directions:
            next_x, next_y = current[0] + dx, current[1] + dy
            next_node = (next_x, next_y)

            if 0 <= next_x < rows and 0 <= next_y < cols and grid[next_x][next_y] != '#' and next_node not in visited:
                new_cost = cost + 1
                heapq.heappush(open_set, (new_cost + heuristic(next_node), next_node))
                parent[next_node] = current

    return None  # No path found


grid = [
    ['S', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '#', '.', '#', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['.', '.', '.', '#', '.', '#', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', 'D', '.']
]

start = (0, 0)  # Starting cell (row, column)
end = (9, 8)    # Destination cell (row, column)

path = a_star(grid, start, end)
print("Shortest Path:", path)
