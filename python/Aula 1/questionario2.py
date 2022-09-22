from unittest import result


def soma_dos_quadrados(x, y):
    qdrx = x * x
    qdry = y * y
    vfinal = qdrx + qdry
    return vfinal


print(soma_dos_quadrados(3, 7))

result = soma_dos_quadrados(3, 7)

frase = "Isso eh um teste"
print(frase[0:8])