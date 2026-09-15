import heapq


# The purpose of this code is to implement Dijkstra's algorithm to find the shortest path from a source node to all other nodes in a weighted graph. The graph is represented as an adjacency list using a dictionary of dictionaries, where each key is a node and its value is another dictionary containing neighboring nodes and their corresponding edge weights.The important piece of information is that Dijkstra's algorithm uses a priority queue (min-heap) to efficiently retrieve the next node with the smallest distance. The algorithm maintains a distance dictionary to track the shortest known distance from the source node to each node in the graph. It iteratively updates these distances based on the weights of the edges connecting nodes.Also, the algorithm ensures that once a node's shortest distance is finalized, it won't be updated again, which is crucial for its correctness. The final output is a dictionary containing the shortest distances from the source node to all other nodes in the graph.
# The code also includes an example graph and demonstrates how to use the Dijkstra's algorithm function to find the shortest distances from a specified source node. The output includes both the graph representation and the computed shortest distances.
# Most importantly is that the algorithm efficiently handles graphs with non-negative weights and provides a clear and concise implementation of Dijkstra's algorithm in Python.Dijkstra's algorithm is particularly useful in various applications, such as network routing, geographical mapping, and any scenario where finding the shortest path is essential. The implementation provided here is a straightforward and effective way to achieve this, leveraging Python's built-in data structures and libraries for optimal performance.This Algorithm is a classic example of a greedy algorithm, where the best local choice (the shortest distance to the next node) leads to a globally optimal solution (the shortest path from the source to all nodes).This algotithm only works with graphs that have non-negative weights, as it assumes that once a node's shortest distance is finalized, it cannot be improved by any subsequent paths. If the graph contains negative weights, other algorithms like Bellman-Ford would be more appropriate.

def dijkstraAlgorithm(graph, src):
    # Distance dictionary with infinity for all nodes except start
    distances = {node: float('inf') for node in graph}
    distances[src] = 0
    
    # Priority queue stores tuples of (current_distance, node)
    pq = [(0, src)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if a shorter path to this node was already processed
        if current_distance > distances[current_node]:
            continue
            
        # Check neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Found a shorter path to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# Example Graph
# Represent the graph as a dictionary of dictionaries
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

# Output the Graph
print("Graph representation (Adjacency List):")
for node, edges in graph.items():
    print(f"{node}: {edges}")
    
# Output the shortest distances from source node 'A'
print("Shortest distances from node 'A':")
print(dijkstraAlgorithm(graph, 'A'))
