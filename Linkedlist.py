class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    node1=Node(10)
    node2=Node(20)
    node3=Node(30)
    node4=Node(40)

    #connecting nodes
    node1.next=node2
    node2.next=node3
    node3.next=node4

    # #print the linked list
    # current=node1
    # while current is not None:
    #     print(current.data ,end="->")
    #     current=current.next
    # print("None")

    #add new node with data(50) at the end 
    new_node=Node(50)
    head=node1
    current=head 

    while current.next is not None:
        current=current.next
    current.next=new_node   

     #print the linked list
    current=node1
    while current is not None:
        print(current.data ,end="->")
        current=current.next
    print("None") 
