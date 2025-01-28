def contar_num(*numeros): 

    lista_pares = []
    lista_impares = []

    for i in numeros: 
        if i % 2 == 0:
            lista_pares.append(i)
        else: 
            lista_impares.append(i)

    cont_par = len(lista_pares)
    cont_impar = len(lista_impares)

    return lista_pares, lista_impares, cont_par, cont_impar
