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
      if self.head is None and self.tail is None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.size += 1
        return
      new_node = Node(value)
      self.tail.next_node = new_node
      new_node.previous_node = self.tail
      self.tail = new_node
      self.size += 1
    
    else:
      print("Reached the limit size!")
  
  def look_at_nodes(self):
    if self.size == 0:
      print("\nNothing to look at!\n")
      return
    
    current_node = self.head
    while True:
      print("\n\n\n" + str(current_node.value) + "\n")
      if current_node == self.head and current_node == self.tail:
        choice = input("Press 'e' for exit: ")
        while choice != 'e':
          print("Press a valid character!")
          choice = input("Press 'e' for exit: ")
        print("Exiting this aspect.")
        break
      
      if current_node == self.head:
        choice = input("Press 'n' for next or 'e' for exit: ")
        while choice not in ['n', 'e']:
          print("Press a valid character!")
          choice = input("Press 'n' for next or 'e' for exit: ")
        if choice == 'n':
          current_node = current_node.next_node
          continue
        elif choice == 'e':
          print("Exiting this aspect.")
          break

      if current_node == self.tail:
        choice = input("Press 'p' for previous or 'e' for exit: ")
        while choice not in ['p', 'e']:
          print("Press a valid character!")
          choice = input("Press 'p' for previous or 'e' for exit: ")
        if choice == 'p':
          current_node = current_node.previous_node
          continue
        elif choice == 'e':
          print("Exiting this aspect.")
          break
      
      choice = input("Press 'n' for next, 'p' for previous or 'e' for exit: ")
      while choice not in ['n', 'p', 'e']:
        print("Press a valid character!")
        choice = input("Press 'n' for next, 'p' for previous or 'e' for exit: ")
      if choice == 'n':
        current_node = current_node.next_node
        continue
      elif choice == 'p':
        current_node = current_node.previous_node
        continue
      elif choice == 'e':
        print("Exiting this aspect.")
        break
  
  def has_space(self):
    return self.size < self.limit


beach = DoublyLinkedList()
beach.add_node("10. Praia do Espelho, Porto Seguro (Bahia)")
beach.add_node("9. Baia dos Golfinhos, Praia da Pipa (Rio Grande do Norte)")
beach.add_node("8. Cacimba do Padre, Fernando de Noronha (Pernambuco)")
beach.add_node("7. Quarta Praia, Morro de Sao Paulo (Bahia)")
beach.add_node("6. Praia dos Carneiros (Pernambuco)")
beach.add_node("5. Praia de Lopes Mendes, Ilha Grande (Rio de Janeiro)")
beach.add_node("4. Jericoacoara (Ceara)")
beach.add_node("3. Praias de Arraial do Cabo (Rio de Janeiro)")
beach.add_node("2. Praia de Sao Miguel dos Milagres (Alagoas)")
beach.add_node("1. Baia do Sancho e Baia dos Porcos (Pernambuco)")

beach.look_at_nodes()