#class to represent given node in a doubly linked list 
class Node:
  #initial a node with potential next and previous nodes, default value of none
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node

#setter method to set next node
  def set_next(self, next_node):
    self.next_node = next_node

#getter method to get next node
  def get_next(self):
    return self.next_node

#setter method to set prev node
  def set_prev(self, prev_node):
    self.prev_node = prev_node

#getter method to get prev node   
  def get_prev(self):
    return self.prev_node

#get value at a given node
  def get_value(self):
    return self.value

#doubly linked list class
class DoublyLinkedList:
  #initialise head and tail values to be none
  def __init__(self):
    self.head_node = None
    self.tail_node = None

#add to the head
  def add_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node #current head is head none

    if current_head != None: #if current head has a value
      current_head.set_prev(new_head) #set the currents head previous node to the new head
      new_head.set_next(current_head) # set the new head's next value to the current head

    self.head_node = new_head #reconfirm the headnode

    if self.tail_node == None: #if tail heads value is = none means the list is empty 
      self.tail_node = new_head #set the tail node equal new head 

#add to tail
  def add_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next(new_tail)
      new_tail.set_prev(current_tail)

    self.tail_node = new_tail

    if self.head_node == None: #if head node is none the list is empty 
      self.head_node = new_tail #set head node to new tail 

#remove head
  def remove_head(self):
    removing_head = self.head_node #store ref

    if removing_head == None: 
        return None # If the list is empty, return None

    self.head_node = removing_head.get_next() # Update the head node reference to the next node

    if self.head_node != None: # Check if the new head node is not None
        self.head_node.set_prev(None) # Set the previous node reference of the new head to None

    if removing_head == self.tail_node: # Check if the removed head node was also the tail node
        self.remove_tail() # If the removed head node was also the tail node, call the remove_tail() method

    return removing_head.get_value() # Return the value of the removed head node


#remove tail
  def remove_tail(self):
    removing_tail = self.tail_node 

    if removing_tail == None:
      return None

    self.tail_node = removing_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next(None)

    if removing_tail == self.head_node:
      self.remove_head()

    return removing_tail.get_value()

def remove_value(self, removing_value):
    removing_node = None # Initialize a variable to track the node to remove
    current_node = self.head_node # Start from the head node and iterate through the list

    while current_node != None: # Iterate until the end of the list is reached
        if current_node.get_value() == removing_value: # Check if the value of the current node matches the removing value
            removing_node = current_node # Set the removing_node to the current node and break the loop
        break

    current_node = current_node.get_next() # Move to the next node

    if removing_node == None: # Check if the removing_node is None (i.e., the value to remove was not found)
        return None # If the value to remove was not found, return None

    if removing_node == self.head_node: # Check if the removing_node is the head node
        self.remove_head() # If the removing_node is the head node, call the remove_head() method
    elif removing_node == self.tail_node: # Check if the removing_node is the tail node
        self.remove_tail() # If the removing_node is the tail node, call the remove_tail() method
    else: # If the removing_node is in the middle of the list
        next_node = removing_node.get_next_node() # Get the next node of the removing_node
        prev_node = removing_node.get_prev_node() # Get the previous node of the removing_node
        next_node.set_prev(prev_node) # Update the previous node reference of the next node
        prev_node.set_next(next_node) # Update the next node reference of the previous node

    return removing_node # Return the removed node


def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list