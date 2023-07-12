package queues;

public class queue {
    class Node {
        private String value;
        private Node nextNode;
        
        public Node(String value) {
          this.value = value;
          this.nextNode = null;
        }
        
        public void setNext(Node nextNode) {
          this.nextNode = nextNode;
        }
        
        public Node getNext() {
          return nextNode;
        }
        
        public String getValue() {
          return value;
        }
      }
      
      class Queue {
        private Node head;
        private Node tail;
        private Integer max_size;
        private Integer size;
        
        public Queue(Integer max_size) {
          this.head = null;
          this.tail = null;
          this.max_size = max_size;
          this.size = 0;
        }
        
        public void enqueue(String value) {
          if (hasSpace()) {
            Node itemToAdd = new Node(value);
            System.out.printf("Adding %s to the queue!%n", itemToAdd.getValue());
            if (isEmpty()) {
              head = itemToAdd;
              tail = itemToAdd;
            } else {
              tail.setNext(itemToAdd);
              tail = itemToAdd;
            }
            size++;
          } else {
            System.out.println("Sorry, no more room!");
          }
        }
        
        public String dequeue() {
          if (getSize() > 0) {
            Node itemToRemove = head;
            System.out.printf("%s is served!%n", itemToRemove.getValue());
            if (getSize() == 1) {
              head = null;
              tail = null;
            } else {
              head = head.getNext();
            }
            size--;
            return itemToRemove.getValue();
          } else {
            System.out.println("The queue is totally empty!");
            return null;
          }
        }
        
        public String peek() {
          if (size > 0) {
            return head.getValue();
          } else {
            System.out.println("No orders waiting!");
            return null;
          }
        }
        
        public int getSize() {
          return size;
        }
        
        public boolean hasSpace() {
          if (max_size == null) {
            return true;
          } else {
            return max_size > getSize();
          }
        }
        
        public boolean isEmpty() {
          return size == 0;
        }
      }
      
    //   public class Main {
    //     public static void main(String[] args) {
    //       System.out.println("Creating a deli line with up to 10 orders...\n------------");
    //       Queue deliLine = Queue(10);
    //       System.out.println("Adding orders to our deli line...\n------------");
    //       deliLine.enqueue("egg and cheese on a roll");
    //       deliLine.enqueue("bacon, egg, and cheese on a roll");
    //       deliLine.enqueue("toasted sesame bagel with butter and jelly");
    //       deliLine.enqueue("toasted roll with butter");
    //       deliLine.enqueue("bacon, egg, and cheese on a plain bagel");
    //       deliLine.enqueue("two fried eggs with home fries and ketchup");
    //       deliLine.enqueue("egg and cheese on a roll with jalapeños");
    //       deliLine.enqueue("plain bagel with plain cream cheese");
    //       deliLine.enqueue("blueberry muffin toasted with butter");
    //       deliLine.enqueue("bacon, egg, and cheese on a roll");
    //       // ------------------------ //
    //       // Uncomment the line below:
    //       deliLine.enqueue("western omelet with home fries");
    //       // ------------------------ //
    //       System.out.println("------------\nOur first order will be " + deliLine.peek());
    //       System.out.println("------------\nNow serving...\n------------");
    //       deliLine.dequeue();
    //       deliLine.dequeue();
    //       deliLine.dequeue();
    //       deliLine.dequeue();
    //       deliLine.dequeue();
    //       deliLine.dequeue();
    //       deliLine.dequeue();
    //       deliLine.dequeue();
    //       deliLine.dequeue();
    //       deliLine.dequeue();
    //       // ------------------------ //
    //       // Uncomment the line below:
    //       deliLine.dequeue();
    //       // ------------------------ //
    //     }
    //   }
      
    

    
    
}
