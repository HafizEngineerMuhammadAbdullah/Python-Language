import random
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


# ==========================================================
# 1. GRAPH VISUALIZATION
# ==========================================================

def draw_graph(graph, path=None, visited=None, source=None, goal=None,
               title="Graph Search Visualizer"):

    path = path or []
    visited = visited or set()

    # Give every node a consistent position in the diagram.
    positions = nx.spring_layout(graph, seed=42, weight="weight")

    path_edges = set()
    for i in range(len(path) - 1):
        path_edges.add(frozenset((path[i], path[i + 1])))

    # Choose colors to explain the search result visually.
    node_colors = []
    for node in graph.nodes():
        if node == source:
            node_colors.append("#2ecc71")  # Green: source
        elif node == goal:
            node_colors.append("#e74c3c")  # Red: goal
        elif node in path:
            node_colors.append("#f1c40f")  # Yellow: successful path
        elif node in visited:
            node_colors.append("#85c1e9")  # Blue: explored
        else:
            node_colors.append("#d5d8dc")  # Gray: unexplored

    edge_colors = []
    edge_widths = []

    for u, v in graph.edges():
        if frozenset((u, v)) in path_edges:
            edge_colors.append("#e67e22")
            edge_widths.append(3.5)
        else:
            edge_colors.append("#aab7b8")
            edge_widths.append(1.5)

    plt.figure(figsize=(10, 7))

    nx.draw_networkx(
        graph,
        pos=positions,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        width=edge_widths,
        node_size=1800,
        font_size=11,
        font_weight="bold",
        edgecolors="#34495e"
    )

    # Show the weight written on each edge.
    weights = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(
        graph, positions, edge_labels=weights, font_size=9
    )

    plt.title(title, fontsize=15, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# ==========================================================
# 2. RANDOM SEARCH
# ==========================================================

def random_search_algo(graph, source, goal):
    # The frontier contains discovered nodes waiting to be explored.
    frontier = [(source, [source])]
    visited = set()

    while frontier:
        index = random.randrange(len(frontier))
        current, path = frontier.pop(index)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path, visited

        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                frontier.append((neighbor, path + [neighbor]))

    return None, visited


# ==========================================================
# 3. OPEN LIST SEARCH
# ==========================================================

def open_list_search_algo(graph, source, goal):
    # Educational variant: use an OPEN list as a FIFO queue.
    open_list = deque([(source, [source])])
    discovered = {source}
    visited = set()

    while open_list:
        current, path = open_list.popleft()
        visited.add(current)

        if current == goal:
            return path, visited

        for neighbor in graph.neighbors(current):
            if neighbor not in discovered:
                discovered.add(neighbor)
                open_list.append((neighbor, path + [neighbor]))

    return None, visited


# ==========================================================
# 4. CLOSED LIST SEARCH
# ==========================================================

def closed_list_search_algo(graph, source, goal):
    # Educational variant: DFS with an explicit CLOSED set.
    open_list = [(source, [source])]
    closed_list = set()

    while open_list:
        current, path = open_list.pop()

        if current in closed_list:
            continue

        closed_list.add(current)

        if current == goal:
            return path, closed_list

        # Reverse neighbors so the traversal order is predictable.
        neighbors = sorted(graph.neighbors(current), reverse=True)

        for neighbor in neighbors:
            if neighbor not in closed_list:
                open_list.append((neighbor, path + [neighbor]))

    return None, closed_list


# ==========================================================
# 5. BREADTH-FIRST SEARCH (BFS)
# ==========================================================

def bfs_search_algo(graph, source, goal):
    queue = deque([source])
    parent = {source: None}
    visited = set()

    while queue:
        current = queue.popleft()
        visited.add(current)

        if current == goal:
            break

        for neighbor in graph.neighbors(current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    if goal not in parent:
        return None, visited

    # Reconstruct the path by walking backward through parents.
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path, visited


# ==========================================================
# 6. DEPTH-FIRST SEARCH (DFS)
# ==========================================================

def dfs_search_algo(graph, source, goal):
    stack = [source]
    parent = {source: None}
    visited = set()

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            break

        neighbors = sorted(graph.neighbors(current), reverse=True)

        for neighbor in neighbors:
            if neighbor not in parent:
                parent[neighbor] = current
                stack.append(neighbor)

    if goal not in visited:
        return None, visited

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path, visited


# ==========================================================
# 7. DIJKSTRA'S / UNIFORM COST SEARCH
# ==========================================================

def dijkstras_search_algo(graph, source, goal):
    # Each heap item contains (total_cost, node).
    priority_queue = [(0, source)]
    distances = {source: 0}
    parent = {source: None}
    visited = set()

    while priority_queue:
        cost, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            break

        for neighbor, data in graph[current].items():
            weight = data["weight"]
            new_cost = cost + weight

            if new_cost < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(
                    priority_queue, (new_cost, neighbor)
                )

    if goal not in distances:
        return None, visited

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path, visited


# ==========================================================
# 8. INPUT HELPERS
# ==========================================================

def read_graph():
    graph = nx.Graph()

    while True:
        raw_nodes = input(
            "\nEnter node names separated by commas (e.g. A,B,C,D): "
        )
        nodes = [node.strip() for node in raw_nodes.split(",")]

        if (not raw_nodes.strip()
                or any(not node for node in nodes)
                or len(nodes) != len(set(nodes))):
            print("Error: enter non-empty, unique node names.")
            continue

        if any("," in node for node in nodes):
            print("Invalid node names.")
            continue

        graph.add_nodes_from(nodes)
        break

    print("\nEnter edges one at a time.")
    print("Format: A,B,4 means an edge from A to B with weight 4.")
    print("Format: A,B means an edge with default weight 1.")
    print("Type DONE when you have finished adding edges.")

    while True:
        raw_edge = input("Edge: ").strip()

        if raw_edge.upper() == "DONE":
            break

        parts = [part.strip() for part in raw_edge.split(",")]

        if len(parts) not in (2, 3):
            print("Invalid format. Use A,B or A,B,4.")
            continue

        u, v = parts[0], parts[1]

        if u not in graph or v not in graph:
            print("Error: both endpoints must be existing nodes.")
            continue

        if u == v:
            print("Self-loops are not supported in this assignment.")
            continue

        try:
            weight = float(parts[2]) if len(parts) == 3 else 1.0
        except ValueError:
            print("Error: weight must be a number.")
            continue

        if weight < 0:
            print("Error: negative weights are not supported.")
            continue

        if not weight < float("inf"):
            print("Error: weight must be finite.")
            continue

        graph.add_edge(u, v, weight=weight)

    if graph.number_of_edges() == 0:
        print("Warning: no edges were entered. Nodes are isolated.")

    return graph


def read_existing_node(graph, prompt):
    while True:
        node = input(prompt).strip()

        if node in graph:
            return node

        print("Error: that node does not exist. Try again.")


# ==========================================================
# 9. MENU AND ALGORITHM INFORMATION
# ==========================================================

ALGORITHMS = {
    "1": (
        "Random Search",
        random_search_algo,
        "O(V + E) expected upper bound",
        "O(V^2) upper bound with stored paths"
    ),
    "2": (
        "Closed List Search (DFS variant)",
        closed_list_search_algo,
        "O(V + E)",
        "O(V^2) upper bound with stored paths"
    ),
    "3": (
        "Open List Search (FIFO variant)",
        open_list_search_algo,
        "O(V + E)",
        "O(V^2) upper bound with stored paths"
    ),
    "4": (
        "Dijkstra's / Uniform Cost Search",
        dijkstras_search_algo,
        "O((V + E) log V)",
        "O(V)"
    ),
    "5": (
        "Breadth-First Search (BFS)",
        bfs_search_algo,
        "O(V + E)",
        "O(V)"
    ),
    "6": (
        "Depth-First Search (DFS)",
        dfs_search_algo,
        "O(V + E)",
        "O(V)"
    ),
}


def main():
    print("=" * 55)
    print("       PYTHON GRAPH SEARCH VISUALIZER")
    print("=" * 55)

    while True:
        try:
            graph = read_graph()

            print("\nYour input graph is ready!")
            draw_graph(graph, title="Your Original Graph")

            while True:
                print("\nChoose a search algorithm:")
                for key, info in ALGORITHMS.items():
                    print(f"{key}. {info[0]}")
                print("7. Exit")

                choice = input("Enter your choice (1-7): ").strip()

                if choice == "7":
                    print("Thank you for using the visualizer!")
                    return

                if choice not in ALGORITHMS:
                    print("Invalid choice. Enter a number from 1 to 7.")
                    continue

                source = read_existing_node(
                    graph, "Enter the source node: "
                )
                goal = read_existing_node(
                    graph, "Enter the goal node: "
                )

                name, algorithm, time_complexity, space_complexity = (
                    ALGORITHMS[choice]
                )

                path, visited = algorithm(graph, source, goal)

                print(f"\nAlgorithm: {name}")
                print(f"Source: {source}")
                print(f"Goal: {goal}")
                print(f"Visited nodes: {', '.join(visited) or 'None'}")

                if path is None:
                    print(f"No path exists from {source} to {goal}.")
                    draw_graph(
                        graph,
                        visited=visited,
                        source=source,
                        goal=goal,
                        title=f"{name}: No Path Found"
                    )
                else:
                    print("Path found:", " -> ".join(path))

                    if choice == "4":
                        total_cost = sum(
                            graph[u][v]["weight"]
                            for u, v in zip(path, path[1:])
                        )
                        print(f"Total path cost: {total_cost:g}")

                    elif choice == "5":
                        print(
                            "Number of edges in path:", len(path) - 1
                        )
                        print(
                            "BFS gives a shortest path by edge count "
                            "in an unweighted graph."
                        )

                    draw_graph(
                        graph,
                        path=path,
                        visited=visited,
                        source=source,
                        goal=goal,
                        title=f"{name}: Path Found"
                    )

                print("\nComplexity analysis:")
                print(f"Time: {time_complexity}")
                print(f"Auxiliary space: {space_complexity}")
                print(
                    "V = number of nodes; E = number of edges. "
                    "Graph storage is excluded."
                )

                again = input(
                    "\nTry another algorithm on the same graph? (y/n): "
                ).strip().lower()

                if again != "y":
                    break

        except (EOFError, KeyboardInterrupt):
            print("\nProgram stopped safely.")
            return
        except Exception as error:
            # A last-resort guard; expected input errors are handled above.
            print(f"Unexpected error: {error}")
            print("Please check your input and try again.")


if __name__ == "__main__":
    main()
