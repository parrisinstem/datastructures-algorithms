package python.linkedlists;

//Class to represent a given node in a linked list

class Node {
    private Integer value;
    private Node nextNode;

    // Constructor to initialize a node with value and potential next node
    public Node(Integer value, Node nextNode) {
        this.value = value;
        this.nextNode = nextNode;
    }

    // Getter method to retrieve value of the node
    public Integer getValue() {
        return value;
    }

    // Getter for retrieving reference to next node
    public Node getNext() {
        return nextNode;
    }

    // Setter method for setting reference to next node
    public void setNext(Node nextNode) {
        this.nextNode = nextNode;
    }
}

// Represent linked list
class LinkedList {
    private Node headNode;

    // Constructor: initialize list lead with a head node
    public LinkedList(Integer value) {
        headNode = new Node(value, null);
    }

    // Getter method for retrieving the head node of the list
    public Node getHead() {
        return headNode;
    }

    // Insert node at the beginning
    public void insertHead(Integer newValue) {
        Node newNode = new Node(newValue, headNode);
        headNode = newNode;
    }

    // Method to remove a node with specific value
    public void removeNode(Integer removingValue) {
        Node currentNode = getHead();
        if (currentNode.getValue() == removingValue) {
            headNode = currentNode.getNext();
        } else {
            while (currentNode != null) {
                Node nextNode = currentNode.getNext();
                if (nextNode.getValue() == removingValue) {
                    currentNode.setNext(nextNode.getNext());
                    currentNode = null;
                } else {
                    currentNode = nextNode;
                }
            }
        }
    }

    // Add each element in list into string value
    public String stringifyList() {
        StringBuilder stringList = new StringBuilder();
        Node currentNode = getHead();
        while (currentNode != null) {
            if (currentNode.getValue() != null) {
                stringList.append(currentNode.getValue()).append("\n");
            }
            currentNode = currentNode.getNext();
        }
        return stringList.toString();
    }

    // Swap elements in a linked list
    public void swapNodes(int val1, int val2) {
        Node prevNode1 = null;
        Node prevNode2 = null;
        Node node1 = headNode;
        Node node2 = headNode;

        if (val1 == val2) {
            System.out.println("Elements are the same - no swap needed");
            return;
        }

        while (node1 != null) {
            if (node1.getValue() == val1) {
                break;
            }
            prevNode1 = node1;
            node1 = node1.getNext();
        }

        while (node2 != null) {
            if (node2.getValue() == val2) {
                break;
            }
            prevNode2 = node2;
            node2 = node2.getNext();
        }

        if (node1 == null || node2 == null) {
            System.out.println("Swap not possible, one or more elements are not in the list");
            return;
        }

        if (prevNode1 == null) {
            headNode = node2;
        } else {
            prevNode1.setNext(node2);
        }

        if (prevNode2 == null) {
            headNode = node1;
        } else {
            prevNode2.setNext(node1);
        }
    }
}
