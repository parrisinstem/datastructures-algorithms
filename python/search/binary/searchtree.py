import random

class BinarySearchTree:
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None

  def insert(self, value):
    # Check if the value is less than the current node's value
    if value < self.value:
      if self.left is None:
        # Insert a new node on the left if it is empty
        self.left = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
      else:
        # Recursively insert the value on the left subtree
        self.left.insert(value)
    else:
      if self.right is None:
        # Insert a new node on the right if it is empty
        self.right = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
      else:
        # Recursively insert the value on the right subtree
        self.right.insert(value)
        
  def get_node_by_value(self, value):
    # Check if the current node's value matches the target value
    if self.value == value:
      return self
    elif self.left is not None and value < self.value:
      # Recursively search the left subtree
      return self.left.get_node_by_value(value)
    elif self.right is not None and value >= self.value:
      # Recursively search the right subtree
      return self.right.get_node_by_value(value)
    else:
      return None
  
  def depth_first_traversal(self):
    if self.left is not None:
      # Traverse the left subtree
      self.left.depth_first_traversal()
    print(f'Depth={self.depth}, Value={self.value}')
    if self.right is not None:
      # Traverse the right subtree
      self.right.depth_first_traversal()


print("Creating Binary Search Tree rooted at value 15:")
tree = BinarySearchTree(15)

for x in range(10):
  # Insert random values into the tree
  tree.insert(random.randint(0, 100))
  
print("Printing the inorder depth-first traversal:")
tree.depth_first_traversal()
