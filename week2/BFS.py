from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def bfs(root):
    if not root:
        return
    
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.value, end=" ")
        for child in current.children:
            queue.append(child)

# Example: Build tree from user input
def build_tree():
    nodes = {}
    n = int(input("Enter number of nodes: "))
    
    for _ in range(n):
        parent_val = input("Enter parent node value: ")
        child_count = int(input(f"Enter number of children for {parent_val}: "))
        
        if parent_val not in nodes:
            nodes[parent_val] = Node(parent_val)
        
        parent = nodes[parent_val]
        
        for _ in range(child_count):
            child_val = input(f"Enter child of {parent_val}: ")
            if child_val not in nodes:
                nodes[child_val] = Node(child_val)
            parent.children.append(nodes[child_val])
    
    root_val = input("Enter root node value: ")
    return nodes[root_val]

# Run BFS
if __name__ == "__main__":
    root = build_tree()
    print("BFS Traversal:")
    bfs(root)
