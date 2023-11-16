class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
       new_node = Node(value)
       if self.head is None:
           self.head = new_node
       else:
           last_node = self.head
           while last_node.next:
               last_node = last_node.next
           last_node.next = new_node

    def delete(self, value):
       if self.head is None:
           return
       if self.head.value == value:
           self.head = self.head.next
           return
       current_node = self.head
       while current_node.next:
           if current_node.next.value == value:
               current_node.next = current_node.next.next
               return
           current_node = current_node.next

    def display(self):
       values = []
       current_node = self.head
       while current_node:
           values.append(str(current_node.value))
           current_node = current_node.next
       return "->".join(values) + "->None"

def linked_list_function(values, deleted_node):
   ll = LinkedList()
   for value in values:
       ll.insert(value)
   ll.delete(deleted_node)
   return ll.display()

result = linked_list_function(values=[1, 2, 3, 2, 4], deleted_node=2)
print(result)                
