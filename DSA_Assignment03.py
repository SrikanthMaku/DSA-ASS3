
 # Binary Tree;

class node:
    def __init__(self,data,left =None,right= None):
        self.data = data
        self.right = right
        self.left=left

    def addnode(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.addnode(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.addnode(data)
        else:
            self.data = data
    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end = ' ')
        if self.right:
            self.right.inorder()
        
    def preorder(self):
        print(self.data, end= ' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end= ' ')
    
    def search(self,value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                if self.left.data:
                    return self.left.search(value)
        if value > self.data:
            if self.right:
                if self.right.data:
                    return self.right.search(value)
        return False
    
    def get_min(self):
        if self.left is None:
            return self.data
        return self.left.get_min()
    
    def get_max(self):
        if self.right is None:
            return self.data
        return self.right.get_max()
    
    
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right.delete(value)
        else: 
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            temp = self.right.get_min() 
            self.data = temp
            self.right = self.right.delete(temp)
        return self       
        



root  = node(50)
root.addnode(42)
root.addnode(78)
root.addnode(67)
root.addnode(34)
root.addnode(45)
root.inorder()
print(" ")
root.preorder()
print(" ")
root.postorder()
print(" ")
print(root.search(42))
print(" ")
print(root.get_max())
print(" ")
print(root.get_min())
root.delete(42)
root.inorder()
print(" ")


# 2

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_height(root):
    if root is None:
        return -1
    left_height = find_height(root.left)
    right_height = find_height(root.right)
    return max(left_height, right_height) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Height of the tree:", find_height(root))



# 3

class node:
    def __init__(self,data,left =None,right= None):
        self.data = data
        self.right = right
        self.left=left

    def addnode(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.addnode(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.addnode(data)
        else:
            self.data = data
    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end = ' ')
        if self.right:
            self.right.inorder()
        
    def preorder(self):
        print(self.data, end= ' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end= ' ')
    
root  = node(50)
root.addnode(42)
root.addnode(78)
root.addnode(67)
root.addnode(34)
root.addnode(45)
print("In-order traversal ")
root.inorder()
print("\n Pre-order traversal ")
root.preorder()
print("\n Post-orer traversal ")
root.postorder()




# 4

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_leaves(root):
    if root is not None:
        if root.left is None and root.right is None:
            print(root.data, end=' ')
        print_leaves(root.left)
        print_leaves(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Leaves in the binary tree:")
print_leaves(root)


# 5


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

root = TreeNode(1)
root.add_child(TreeNode(2))
root.add_child(TreeNode(3))
root.add_child(TreeNode(4))

root.children[0].add_child(TreeNode(5))
root.children[0].add_child(TreeNode(6))
root.children[2].add_child(TreeNode(7))
root.children[2].add_child(TreeNode(8))

# BFS Implementation
def bfs(tree):
    queue = [tree]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.value)
        queue.extend(node.children)
    return result

# DFS Implementation
def dfs(tree):
    stack = [tree]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.value)
        stack.extend(reversed(node.children))
    return result

print("BFS traversal:", bfs(root))
print("DFS traversal:", dfs(root))


# 6

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_left_leaves(root):
    if not root:
        return 0

    def is_leaf(node):
        return node and not node.left and not node.right

    def traverse(node):
        total_sum = 0

        if node.left:
            if is_leaf(node.left):
                total_sum += node.left.val
            else:
                total_sum += traverse(node.left)

        if node.right:
            total_sum += traverse(node.right)

        return total_sum

    return traverse(root)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sum_of_left_leaves(root)) 


# 7

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_perfect_binary_tree_sum(root):
    if root is None:
        return 0

    return root.data + get_perfect_binary_tree_sum(root.left) + get_perfect_binary_tree_sum(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

sum_of_nodes = get_perfect_binary_tree_sum(root)
print("Sum of all nodes in the perfect binary tree:", sum_of_nodes)


# 8

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_subtrees_with_sum(root, x):
    count = 0
    def dfs(node):
        nonlocal count
        if not node:
            return 0
        
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
        current_sum = node.value + left_sum + right_sum
        
        if current_sum == x:
            count += 1
            
        return current_sum
    
    dfs(root)
    return count


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

x = 8
result = count_subtrees_with_sum(root, x)
print("Number of subtrees that sum up to", x, ":", result)





# 9

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_level_sum(root):
    if not root:
        return 0

    max_sum = root.value
    queue = [root]

    while queue:
        level_sum = 0
        level_size = len(queue)

        for i in range(level_size):
            node = queue.pop(0)
            level_sum += node.value

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        max_sum = max(max_sum, level_sum)

    return max_sum


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(7)

result = max_level_sum(root)
print("Maximum level sum in the binary tree:", result)



# 10

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_odd_level_nodes(root):
    def dfs(node, level):
        if not node:
            return
        
        if level % 2 != 0:
            print(node.value, end=" ")

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 1)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(7)

print("Nodes at odd levels of the binary tree:")
print_odd_level_nodes(root)






