from code_behind_Pcs102 import Node, DoublyLinkedList

ideas_of_aspects = ["beach", "museum", "aquarium", "art gallery", "monument", "cave", "countryside", "big city"]

# Aspects instances:
beach = DoublyLinkedList()
museum = DoublyLinkedList()


# Aspects values:
beach_node_values = ["10. Praia do Espelho, Porto Seguro (Bahia)", "9. Baia dos Golfinhos, Praia da Pipa (Rio Grande do Norte)", "8. Cacimba do Padre, Fernando de Noronha (Pernambuco)", "7. Quarta Praia, Morro de Sao Paulo (Bahia)", "6. Praia dos Carneiros (Pernambuco)", "5. Praia de Lopes Mendes, Ilha Grande (Rio de Janeiro)", "4. Jericoacoara (Ceara)", "3. Praias de Arraial do Cabo (Rio de Janeiro)", "2. Praia de Sao Miguel dos Milagres (Alagoas)", "1. Baia do Sancho e Baia dos Porcos (Pernambuco)"]
for value in beach_node_values:
  beach.add_node(value)

museum_node_values = ["10. Museu de Ciencias e Tecnologia da PUC, Porto Alegre (Rio Grande do Sul)", "9. Museu do Futebol, Sao Paulo (Sao Paulo)", "8. Museu Imperial, Petropolis (Rio de Janeiro)", "7. Museu de Arte de Sao Paulo, Sao Paulo (Sao Paulo)", "6. Catavento Cultural e Educacional, Sao Paulo (Sao Paulo)", "5. Inhotim, Brumadinho (Minas Gerais)", "4. Museu do Amanha, Rio de Janeiro (Rio de Janeiro)", "3. Oscar Niemeyer, Curitiba (Parana)", "2. Pinacoteca, Sao Paulo (Sao Paulo)", "1. Museu Ricardo Brennand, Recife (Pernambuco)"]
for value in museum_node_values:
  museum.add_node(value)


# Main aspects dictionary:
aspects = {"beach": beach, "museum": museum}


# Main program:
while True:
  aspects["beach"].look_at_nodes()

  break