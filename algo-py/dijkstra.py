

def dijkstra_algo(graph):

    INF = float("infinity")

    unvisited_min_distances = {vertex: INF for vertex in graph}
    visited_vertices = {}
    current_vertex = "U"  # The start node.
    unvisited_min_distances[current_vertex] = 0

    # While vertices remain unvisited
    while len(unvisited_min_distances) > 0:
        # Visit unvisited vertex with smallest known distance from start vertex.
        current_vertex, current_distance = sorted(unvisited_min_distances.items(), key=lambda x: x[1])[
            0]  # Very inefficient - use priority queue in "real" version.
        # For each unvisited neighbour of the current vertex
        for neighbour, neighbour_distance in graph[current_vertex].items():
            # If a neighbour has been processed, skip it.
            if neighbour in visited_vertices:
                continue
            # Calculate the new distance if this route is taken.
            potential_new_distance = current_distance + neighbour_distance
            # If the calculated distance of this vertex is less than the known distance
            if potential_new_distance < unvisited_min_distances[neighbour]:
                # Update the distance for this neighbour.
                unvisited_min_distances[neighbour] = potential_new_distance
        # Add the current vertex to the visited vertices.
        visited_vertices[current_vertex] = current_distance
        # Remove the current vertex from the unvisited list (dictionary).
        del unvisited_min_distances[current_vertex]

    return sorted(visited_vertices.items())


graph = {
    "U": {"V": 6, "W": 7},
    "V": {"U": 6, "X": 10},
    "W": {"U": 7, "X": 1},
    "X": {"W": 1, "V": 10}
}