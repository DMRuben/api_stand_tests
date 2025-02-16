

def suma_menores(lista):
    resultado= 0
    for n in lista:
        if 0 < n < 1000:
            resultado += n


print(resultado)

lista_numeros = [-5, 98, 2, 2000]
suma_menores(lista_numeros)