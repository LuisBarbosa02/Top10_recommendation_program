from code_behind_Pcs102 import Node, DoublyLinkedList


# Aspects instances:
beach = DoublyLinkedList()
museum = DoublyLinkedList()
aquarium = DoublyLinkedList()
zoo = DoublyLinkedList()
monument = DoublyLinkedList()


# Aspects values:
beach_node_values = ["10. Praia do Espelho, Porto Seguro (Bahia)", "9. Baia dos Golfinhos, Praia da Pipa (Rio Grande do Norte)", "8. Cacimba do Padre, Fernando de Noronha (Pernambuco)", "7. Quarta Praia, Morro de Sao Paulo (Bahia)", "6. Praia dos Carneiros (Pernambuco)", "5. Praia de Lopes Mendes, Ilha Grande (Rio de Janeiro)", "4. Jericoacoara (Ceara)", "3. Praias de Arraial do Cabo (Rio de Janeiro)", "2. Praia de Sao Miguel dos Milagres (Alagoas)", "1. Baia do Sancho e Baia dos Porcos (Pernambuco)"]
for value in beach_node_values:
  beach.add_node(value)

museum_node_values = ["10. Museu de Ciencias e Tecnologia da PUC, Porto Alegre (Rio Grande do Sul)", "9. Museu do Futebol, Sao Paulo (Sao Paulo)", "8. Museu Imperial, Petropolis (Rio de Janeiro)", "7. Museu de Arte de Sao Paulo, Sao Paulo (Sao Paulo)", "6. Catavento Cultural e Educacional, Sao Paulo (Sao Paulo)", "5. Inhotim, Brumadinho (Minas Gerais)", "4. Museu do Amanha, Rio de Janeiro (Rio de Janeiro)", "3. Oscar Niemeyer, Curitiba (Parana)", "2. Pinacoteca, Sao Paulo (Sao Paulo)", "1. Museu Ricardo Brennand, Recife (Pernambuco)"]
for value in museum_node_values:
  museum.add_node(value)

aquarium_node_values = ["10. Aquario Natural, Bonito (Mato Grosso do Sul)", "9. Aquario de Paranagua, Paranagua (Parana)", "8. Acqua Mundo, Guaruja (Sao Paulo)", "7. Aquario Natal, Extremoz (Rio Grande do Norte)", "6. Oceanic Aquarium, Balneario Camboriu (Santa Catarina)", "5. Oceanario de Aracaju, Aracaju (Sergipe)", "4. Aquario de Ubatuba, Ubatuba (Sao Paulo)", "3. Aquario Municipal de Santos, Santos (Sao Paulo)", "2. Aquario de Sao Paulo, Sao Paulo (Sao Paulo)", "1. AquaRio, Rio de Janeiro (RJ)"]
for value in aquarium_node_values:
  aquarium.add_node(value)

zoo_node_values = ["10. Zoologico do CIGS, Manaus (Amazonas)", "9. Zooparque Itatiba, Itatiba (Sao Paulo)", "8. Parque Zoologico de Sapucaia do Sul, Sapucaia do Sul (Rio Grande do Sul)", "7. Zoologico Municipal de Guarulhos, Guarulhos (Sao Paulo)", "6. Zoologico de Brasilia, Brasilia (Distrito Federal)", "5. Zoo Pomerode, Pomerode (Santa Catarina)", "4. Zoologico Municipal Quinzinho de Barros, Sorocaba (Sao Paulo)", "3. Zoologico Municipal de Curitiba, Curitiba (Parana)", "2. BioParque do Rio, Rio de Janeiro (Rio de Janeiro)", "1. Zoologico de Sao Paulo, Sao Paulo (Sao Paulo)"]
for value in zoo_node_values:
  zoo.add_node(value)

monument_node_values = ["10. Igreja Sao Francisco de Assis", "9. Teatro Amazonas", "8. Opera de Arame", "7. Museu Oscar Niemeyer", "6. Catedral da Se", "5. Elevador Lacerda", "4. Pao de Acucar", "3. Marco Zero Macapa", "2. Praca dos Tres Poderes", "1. Cristo Redentor"]
for value in monument_node_values:
  monument.add_node(value)


# Main aspects dictionary:
aspects = {"beach": beach, "museum": museum, "aquarium": aquarium, "zoo": zoo, "monument": monument}


# Main program:
print("\n\nTop 10 types of places that you can go in Brazil!")
while True:
  print("\n\n")
  choice = input("Press the first letter of the type of the place that you're interested to go: ")
  autocomplete_result = []
  for x in [x for x in aspects.keys()]:
    if choice == x[0]:
      autocomplete_result.append(x)

  if not autocomplete_result:
    print("\nThere's no type of place with that first letter.\n")
    choice = input("Want to see all the types of places available? Press 'y' for yes or 'n' for no: ")
    while choice not in ['y', 'n']:
      print("\nType a valid character!")
      choice = input("Want to see all the types of places available? ")
    if choice == 'y':
      print(f"\n{[x for x in aspects.keys()]}")
    continue
  elif autocomplete_result:
    print(f"\nThe result of your choice:\n{autocomplete_result}\n")
    choice = input("Write the word of the type: ")
    if choice == "beach":
      aspects["beach"].look_at_nodes()
    elif choice == "museum":
      aspects["museum"].look_at_nodes()
    elif choice == "aquarium":
      aspects["aquarium"].look_at_nodes()
    elif choice == "zoo":
      aspects["zoo"].look_at_nodes()
    elif choice == "monument":
      aspects["monument"].look_at_nodes()
  
  print("")
  see_another_type = input("Do you want to see another type of place? Type 'y' for yes or 'n' for no: ")
  print("")
  while see_another_type not in ['y', 'n']:
    print("Type a valid character!")
    see_another_type = input("Do you want to see another type of place? Type 'y' for yes or 'n' for no: ")
  if see_another_type == 'y':
    continue
  elif see_another_type == 'n':
    break