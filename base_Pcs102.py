ideas_of_aspects = ["beach", "museum", "aquarium", "art gallery", "monument", "cave", "countryside", "big city"]

class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None
    self.previous_node = None


class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
    self.limit = 10

  def add_node(self, value):
    if self.has_space():
      if not self.head and not self.tail:
        self.head = Node(value)
        self.tail = Node(value)
        self.size += 1
        return
      new_node = Node(value)
      self.tail.next_node = new_node
      new_node.previous_node = self.tail
      self.tail = new_node
      self.size += 1
    
    else:
      print("Reached the limit size!")

  def has_space(self):
    return self.size < self.limit