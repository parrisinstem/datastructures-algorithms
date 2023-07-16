
#Class to represent a given node in a linkedin list 
class Node:
    #constructor to initialise a node with value and potentil next node
    def __init__(self,value, next_node = None):
        self.value = value 
        self.next_node = next_node
    
    #gettet value method to retrive value of node
    def get_value(self):
        return self.value 
    
    #getter for retrieving ref to next node
    def get_next(self):
        return self.next_node 
    
    #setter method for setting ref to next node
    def set_next(self, next_node):
        self.next_node = next_node 

#represent linkedlist 
class LinkedList:
    #Constrcutor: initialise list lead with a head node
    def __init__(self, value=None):
        self.head_node = Node(value)
    
    #getter method for retieving the head node of list 
    def get_head(self):
        return self.head_node 
    
    #insert node at beginning
    def insert_head(self, new_value):
        new_node = Node(new_value)
        new_node.set_next(self.head_node)
        self.head_node = new_node

    #method to remove a node with specific value 
    def remove_node(self, removing_value):
        current_node = self.get_head() #current is head
        if current_node.get_value == removing_value: #if current = node we want to remove
            self.head_node = current_node.get_next() #next node ref is assigned to head node
        else:
            while current_node: #conditional 
                next_node = current_node.get_next() #get the next node of current
                if next_node.get_value() == removing_value: #if value of next node equals value we want to remove
                    current_node.set_next(next_node.get_next()) #eliminate the node
                    current_node = None #breaks the while loop
                else:
                    current_node = next_node #move onto the next node 
                
    #add each element in list into string value 
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value())+ "\n"
            current_node = current_node.get_next()
        return string_list



    #swap elements in a linked list 
    def swap_nodes(list, val1, val2):

        prev_node1 = None
        prev_node2 = None
        node1 = list.head_node
        node2 = list.head_node

        if val1 == val2:
            print("Elements are the same - no swap needed")
            return 
        
        while node1 != None:
            if node1.get_value() == val1:
                break 
            prev_node1 = node1
            node1 = node1.get_next()

        while node2 != None:
            if node2.get_value() == val1:
                break 
            prev_node2 = node2
            node2 = node1.get_next()

        if (node1 == None or node2 == None):
            print("Swap not possible, one or more element is not in the list")

        if prev_node1 == None:
            list.head_node = node2
        else:
            prev_node1.set_next(node2)

        if prev_node2 == None:
            list.head_node = node1
        else:
            prev_node2.set_next(node1)

        