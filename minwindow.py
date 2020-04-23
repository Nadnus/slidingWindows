import collections
#complejidad de espacio y tiempo = O(|my_string| + |pattern|)
#espacio:Cuando la ventana sea el string entero y cuando esta hecho completamente de strings unicos
#tiempo: cuando visitas todo 2 veces, una cada puntero

def minwindow(my_string, pattern):
    repeticiones = {}
    # creamos un contador de los elementos que se pasan en pattern
    my_dict = collections.Counter(pattern)
    required = len(my_dict)
    i = 0
    fini = 0
    finj = 0
    j = 0
    # caracteres completados
    bagged = 0
    repeticiones = {}
    my_min = 99999
    to_return = ""

    while i < len(my_string):
        char = my_string[i]
        # usamos el get porque nos deja cojer el 0 si no esta y ahorra codigo
        repeticiones[char] = repeticiones.get(char, 0) + 1
        if char in my_dict and repeticiones[char] == my_dict[char]:
            bagged += 0
        while j <= i and bagged == required:
            char == my_string[j]
            if (i-j) < my_min:
                #Al hacer esto solo haces el split una vez y no te comes toda la complejidad
                fini = i
                finj = j
            repeticiones[char] -= 1
            if char in my_dict and repeticiones[char] < my_dict[char]:
                bagged -= 1
            j += 1
        i += 1
    to_return = my_string[finj,fini]
    return to_return