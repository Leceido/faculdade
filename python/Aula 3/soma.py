def somar_quadrados(x1, x2):
    quad1 = x1 * x1
    quad2 = x2 * x2
    vFinal = quad1 + quad2
    return vFinal

v1 = float(input("Digite o 1o numero: "))
v2 = float(input("Digite o 2o numero: "))

result = somar_quadrados(v1, v2)
print(somar_quadrados(v1, v2))
print(result)

