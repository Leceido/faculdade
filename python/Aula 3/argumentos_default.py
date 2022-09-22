def funcao_imprimir(fruta = "pera", bebida = "agua", sobremesa = "bolo"):
    print(fruta, bebida, sobremesa)

funcao_imprimir(bebida="refrigerante", fruta="banana", sobremesa="pudim") #dessa maneira consegue especificar o que cada parametro vai receber sem precisar ser em ordem
funcao_imprimir("banana", "refrigerante", "pudim") #os parametros serao recebidos na ordem
funcao_imprimir(fruta = "banana") #vai imprimir com os parametros default da funcao