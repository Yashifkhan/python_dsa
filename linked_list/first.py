# print("learn linked list ")

# class Node:
#     def __init__(self,value):
#         self.data=value
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.n=0

#     def __len__(self):
#         return self.n
    
#     def insert_node(self,value):
#         new_node=Node(value)
#         new_node.next=self.head

#         self.head=new_node

#         self.n=self.n+1

#     def __str__(self):
#         current=self.head
#         result=""
#         while current != None:
#             result=result+ str(current.data) + '->'
#             current=current.next

#         return result[:-2]
    
#     def append(self,value):
#         new_node=Node(value)


#         if self.head== None:
#             self.head=new_node
#             self.n=self.n+1
#             return 

#         current=self.head

#         while current != None:
#             current=current.next

#         current.next=new_node
#         self.n=self.n+1

# L=LinkedList()
# L.insert_node(1)
# L.insert_node(2)
# L.insert_node(3)
# L.insert_node(4)
# L.insert_node(40)

# print(L)


print("learn linked list ")

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.n=0

    def __len__(self):
        return self.n
    
    def insert_node(self,value):
        new_node=Node(value)
        new_node.next=self.head

        self.head=new_node

        self.n=self.n+1

    def __str__(self):
        current=self.head
        result=""
        while current != None:
            result=result+ str(current.data) + '->'
            current=current.next

        return result[:-2]
    
    def append(self,value):
        new_node=Node(value)


        if self.head== None:
            self.head=new_node
            self.n=self.n+1
            return 

        current=self.head

        while current != None:
            current=current.next

        current.next=new_node
        self.n=self.n+1

L=LinkedList()
L.insert_node(1)
L.insert_node(2)
L.insert_node(3)
L.insert_node(4)
L.insert_node(40)

print(L)