def sumar_simple(a, b):
    '''
    Permite sumar 2 valores
    '''
    return a+b


def sumar_n_numeros(*numeros):
    '''
    Permite sumar múltiples valores
    '''
    total = 0
    for numero in numeros:
        total += numero
        