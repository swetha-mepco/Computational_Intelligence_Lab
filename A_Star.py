//Informed Search Strategy
//A* Algorithm
def create_graph():
    return {}, {}  # graph, heuristics

def add_node(graph, heuristics, node):
    if node not in graph:
        graph[node] = []
        heuristics[node] = 0
        print("Node added successfully")
    else:
        print("Node already exists")

def add_edge(graph, u, v, weight):
    if u in graph and v in graph:
        graph[u].append((v, weight))
        print("Edge added successfully")
    else:
        print("One or both nodes not found")

def delete_node(graph, heuristics, node):
    if node in graph:
        del graph[node]
        del heuristics[node]
        for u in graph:
            graph[u] = [(v, w) for v, w in graph[u] if v != node]
        print("Node and its edges deleted")
    else:
        print("Node not found")

def delete_edge(graph, u, v):
    if u in graph:
        graph[u] = [(node, w) for node, w in graph[u] if node != v]
        print("Edge deleted successfully")
    else:
        print("Node not found")

def display_graph(graph, heuristics):
    print("\nGraph (Adjacency List + Heuristic):")
    for node in graph:
        print(f"{node} -> {graph[node]} | h = {heuristics[node]}")

def display_adjacency_list(graph, node):
    if node in graph:
        print(f"Adjacency list of {node}: {graph[node]}")
    else:
        print("Node not found")

# ------------------------ A* SEARCH FUNCTIONS ------------------------
def get_min_f(open_list):
    min_index = 0
    for i in range(1, len(open_list)):
        if open_list[i][0] < open_list[min_index][0]:
            min_index = i
    return open_list.pop(min_index)

def a_star(graph, heuristic, start, goal):
    open_list = [(heuristic.get(start, 0), start, [start], 0)]  # f, node, path, g
    closed_list = set()

    while open_list:
        f, current, path, g = get_min_f(open_list)

        if current == goal:
            return path, g

        closed_list.add(current)

        for neighbour, cost in graph.get(current, []):
            if neighbour not in closed_list:
                new_g = g + cost
                new_h = heuristic.get(neighbour, 0)
                new_f = new_g + new_h
                open_list.append((new_f, neighbour, path + [neighbour], new_g))

    return None, float('inf')

def all_paths(graph, start, goal):
    paths = []

    def dfs(node, path, cost):
        if node == goal:
            paths.append((path[:], cost))
            return
        for neighbour, edge_cost in graph.get(node, []):
            if neighbour not in path:
                path.append(neighbour)
                dfs(neighbour, path, cost + edge_cost)
                path.pop()

    dfs(start, [start], 0)
    return paths

# ------------------------ MENU ------------------------
graph, heuristics = create_graph()

while True:
    print("\n1. Add Node")
    print("2. Add Edge (with weight)")
    print("3. Delete Node")
    print("4. Delete Edge")
    print("5. Display Graph")
    print("6. Display Node Adjacency List")
    print("7. Perform A* Search")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        node = input("Enter node: ")
        add_node(graph, heuristics, node)

    elif choice == 2:
        u = input("Enter source node: ")
        v = input("Enter destination node: ")
        w = int(input("Enter weight: "))
        add_edge(graph, u, v, w)

    elif choice == 3:
        node = input("Enter node to delete: ")
        delete_node(graph, heuristics, node)

    elif choice == 4:
        u = input("Enter source node: ")
        v = input("Enter destination node: ")
        delete_edge(graph, u, v)

    elif choice == 5:
        display_graph(graph, heuristics)

    elif choice == 6:
        node = input("Enter node: ")
        display_adjacency_list(graph, node)

    elif choice == 7:
        start = input("Enter start node: ")
        goal = input("Enter goal node: ")

        if start in graph and goal in graph:
            heuristics[goal] = 0  # Goal heuristic is always zero

            print("\nEnter heuristic values for remaining nodes (optional, press Enter to skip):")
            for node in graph:
                if node != goal:
                    value = input(f"Heuristic for {node} (current: {heuristics[node]}): ")
                    if value.strip() != "":
                        heuristics[node] = int(value)

            print("\n--- A* Search ---")
            path, cost = a_star(graph, heuristics, start, goal)
            if path:
                print("Optimal Path:", " -> ".join(path), "| Cost:", cost)
            else:
                print("No path found")

            print("\n--- All Possible Paths ---")
            paths = all_paths(graph, start, goal)
            if paths:
                for p, c in paths:
                    print("Path:", " -> ".join(p), "| Cost:", c)
            else:
                print("No paths available")
        else:
            print("Invalid start or goal node")

    elif choice == 8:
        print("Exiting program")
        break

    else:
        print("Invalid choice")


