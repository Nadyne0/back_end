numeros = [1, 2, 3, 4, 5]
strings = ["a", "b", "c", "d"]


def concatenar_listas(lista_numeros, lista_strings):
    lista_concatenada = []

    for numero in lista_numeros:
        lista_concatenada.append(numero)

    for string in lista_strings:
        lista_concatenada.append(string)

    return lista_concatenada


resultado = concatenar_listas(numeros, strings)


print(resultado)
