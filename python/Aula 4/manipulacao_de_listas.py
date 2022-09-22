from traceback import print_tb


list01 = [0, 3, 4, 5, 6, 2]
list02 = list01
list03 = list01.copy()
print("01A: ", list01)
list01[2] = 0
print("01B: ", list01)
print("02: ", list02)
print("03: ", list03)

num1 = 7
list01.append(num1)
print(list01)
list01.append([2, 4, 6, 4, 2, 1, 3])
print(list01)

list01.clear()
print(list01, list02)

list01.append(list03)
print(list01)
list01.extend(list03)
print(list01)

val1 = list01.count(4)
print(val1)

#index() 
# retorna o index do elemento da lista
# recomendado usar um if 
# pq caso nao tenha o valor na lista o programa vai fechar

#-------------#

#insert(posicao, valor) para inserir um valor em uma posicao especifica

#-------------#

#pop() remove o ultimo elemento ou de uma determinada posicao pop(posicao)

#-------------#

#remove(valor) remove o primeiro valor encontrado

#-------------#

#reverse() e sort()
#reverse inverte a lista e o sort ordena os valores em ordem alfabetica ou numerica

#-------------#
