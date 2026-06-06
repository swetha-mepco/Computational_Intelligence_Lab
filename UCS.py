//Uninformed Search Strategies
//Uniform Cost Search (UCS)
class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}
            print(f"Node {node} added")
        else:
            print(f"Node {node} already exists")

    def add_edge(self, n1, n2, weight=1):
        if n1 not in self.graph:
            self.add_node(n1)
        if n2 not in self.graph:
            self.add_node(n2)
        if n2 not in self.graph[n1]:
            self.graph[n1][n2] = weight
            self.graph[n2][n1] = weight  # Ensure the edge is bidirectional
            print(f"Edge between {n1} and {n2} with weight {weight} added")
        else:
            print("Edge already exists")

    def delete_node(self, node):
        if node in self.graph:
            # Remove all edges associated with the node
            for neighbor in list(self.graph[node].keys()):
                del self.graph[neighbor][node]
            del self.graph[node]
            print(f"Node {node} deleted")
        else:
            print(f"Node {node} does not exist")

    def delete_edge(self, n1, n2):
        if n1 in self.graph and n2 in self.graph[n1]:
            del self.graph[n1][n2]
            del self.graph[n2][n1]  # Ensure the edge is bidirectional
            print(f"Edge between {n1} and {n2} deleted")
        else:
            print(f"Edge between {n1} and {n2} does not exist")

    def display_graph(self):
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")

    def display_adjacency_list(self, node):
        if node in self.graph:
            print(f"Adjacency list for {node}: {self.graph[node]}")
        else:
            print(f"Node {node} does not exist")

    def uniform_cost_search(self, start, end):
        visited = set()
        frontier = [(0, start, [start])]  # List of tuples (cost, node, path)
        path_cost = {start: 0}
        parent = {start: None}

        while frontier:
            # Sort the frontier to get the node with the lowest cost
            frontier.sort(key=lambda x: x[0])
            current_cost, current_node, path = frontier.pop(0)  # Get the lowest cost node and its path

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == end:
                # Reconstruct path
                self.print_path_cost(path, current_cost)
                return

            for neighbor, weight in self.graph[current_node].items():
                if neighbor not in visited:
                    new_cost = current_cost + weight
                    if neighbor not in path_cost or new_cost < path_cost[neighbor]:
                        path_cost[neighbor] = new_cost
                        parent[neighbor] = current_node
                        frontier.append((new_cost, neighbor, path + [neighbor]))

        # If we exit the loop without finding the destination
        print(f"No path found from {start} to {end}. Last reached node: {current_node}. Path taken: {' -> '.join(path)}")

    def print_path_cost(self, path, total_cost):
        print(f"Path found: {' -> '.join(path)} with total cost: {total_cost}")

def main():
    g = Graph()
    print("\nChoose operation:")
    print("1. Add node")
    print("2. Add edge")
    print("3. Display graph")
    print("4. Uniform Cost Search")
    print("5. Delete node")
    print("6. Delete edge")
    print("7. Display adjacency list of a node")
    print("8. Exit")
    while True:
        choice = input("\nEnter choice (1-8): ")

        if choice == "1":
            node = input("Enter node to add: ")
            g.add_node(node)
        elif choice == "2":
            node1 = input("Enter first node: ")
            node2 = input("Enter second node: ")
            weight = int(input("Enter weight for the edge: "))
            g.add_edge(node1, node2, weight)
        elif choice == "3":
            print("Graph adjacency list:")
            g.display_graph()
        elif choice == "4":
            start = input("Enter start node for UCS: ")
            end = input("Enter destination node for UCS: ")
            print(f"Uniform Cost Search from {start} to {end} : ")
            g.uniform_cost_search(start, end)
            print()
        elif choice == "5":
            node = input("Enter node to delete: ")
            g.delete_node(node)
        elif choice == "6":
            node1 = input("Enter first node of the edge to delete: ")
            node2 = input("Enter second node of the edge to delete: ")
            g.delete_edge(node1, node2)
        elif choice == "7":
            node = input("Enter node to display its adjacency list: ")
            g.display_adjacency_list(node)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

