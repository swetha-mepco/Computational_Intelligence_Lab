//Uninformed Search Strategies
//Breadth First Search and Depth First Search
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []
            print(f"Node '{node}' added")
            return True
        print(f"Node '{node}' already exists")
        return False

    def add_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)
                self.adj_list[v].append(u)
                print(f"Edge added between {u} and {v}")
                return True
            else:
                print(f"Edge already exists")
                return False
        return False

    def delete_node(self, n):
        if n in self.adj_list:
            for i in self.adj_list[n]:
                self.adj_list[i].remove(n)
            del self.adj_list[n]
            print(f"Node '{n}' and all its connections are deleted")
            return True
        else:
            print(f"Node '{n}' not found")
            return False

    def delete_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)
                self.adj_list[v].remove(u)
                print(f"Edge between {u} and {v} deleted")
                return True
        print(f"Edge does not exist")
        return False

    def display_graph(self):
        print("\n--- Current Graph ---")
        if not self.adj_list:
            print("The graph is empty")
        for node, neighbours in self.adj_list.items():
            print(f"{node}: {', '.join(neighbours)}")

    def bfs(self, start, end):
        if start not in self.adj_list:
            print("Start node not found")
            return

        visited = [start]
        queue = [start]
        path_found = False

        print(f"BFS traversal from {start}: ", end="")
        print(start, end=" ")
        while queue:
            current = queue.pop(0)
            if current == end:
                path_found = True
                break
            for i in self.adj_list[current]:
                if i not in visited:
                    print(i, end=" ")
                    visited.append(i)
                    if i == end:
                        return
                    queue.append(i)

        print()
        if not path_found and end:
            print(f"Node '{end}' could not be reached")

    def display_node_adj(self, node):
        if node in self.adj_list:
            neighbours = self.adj_list[node]
            print(f"Adjacency list for node '{node}': {', '.join(neighbours) if neighbours else 'Empty'}")
        else:
            print(f"Node '{node}' does not exist")

    def dfs(self, start, end, visited):
        print(start, end=" ")
        visited.append(start)
        if start == end:
            print("\ndestination found")
            return True
        for i in self.adj_list[start]:
            if i not in visited:
                if self.dfs(i, end, visited):
                    return True
        return False

    def dfsTraversal(self, start, end):
        if start not in self.adj_list:
            print("Source not found")
            return
        visited = []
        print("DFS Traversal")
        if not self.dfs(start, end, visited):
            print("Destination not found")

# Example usage menu (same as your original script)

"""def dfs(self,start,end,visited=None):
   if visited in None:
      visited=[]
   print(start,end=" ")
   visited.append(start)
   if start==end:
      print("Destination Found")
      return True
   if not self.dfs(start,end):
      print("No Path Found")
      return False

   for i in self.list[start]:
      if i not in visited:
         if self.dfs(i,end,visited):
            return True

"""

g = Graph()
print("\nMENU")
print("\n1.Add Node\n2.Add Edge\n3.Delete Node\n4.Delete Edge\n5.Display Node Adjacency\n6.Display Graph\n7.BFS Traversal\n8.DFS Traversal\n9.Exit\n")
while True:
    ch = input("Enter your choice: ")

    if ch == "1":
        n = input("Enter node name: ")
        g.add_node(n)
    elif ch == "2":
        u = input("Enter 1st node: ")
        v = input("Enter 2nd node: ")
        g.add_edge(u, v)
    elif ch == "3":
        n = input("Enter node to delete: ")
        g.delete_node(n)
    elif ch == "4":
        u = input("Enter start node of edge: ")
        v = input("Enter end node of edge: ")
        g.delete_edge(u, v)
    elif ch == "5":
        n = input("Enter node name: ")
        g.display_node_adj(n)
    elif ch == "6":
        g.display_graph()
    elif ch == "7":
        s = input("Enter start node: ")
        e = input("Enter target node : ")
        g.bfs(s, e if e else None)
    elif ch == "9":
        print("Exiting....")
        break
    elif ch == "8":
        s = input("Enter source node: ")
        d = input("Enter destination node: ")
        g.dfsTraversal(s, d)
    else:
        print("Invalid input")

