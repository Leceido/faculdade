def primeira_funcao():
    def segunda_funcao():
        print(x + 1)
    x = 10
    print(x * a)
    segunda_funcao()

a = 5
primeira_funcao()

print("#---------------------------#")

def funcao_com_variavel(par1):
    x = 20
    return (x * par1)

valor01 = funcao_com_variavel(5)
print(valor01)
#print(x) tentar imprimir o x da erro pois o x eh uma variavel de escopo local da funcao

print("#---------------------------#")

def imprimir_a():
    a = 12 #variavel local
    print(a)

a = 10 #variavel global
imprimir_a() #vai imprimir 12
print(a) #vai imprimir 10

print("#---------------------------#")

def imprimir_a2():
    global a #declara que a variavel "a" da funcao eh global
    a = 12 #altera o valor da variavel "a" global
    print(a)

imprimir_a2()
print(a)
