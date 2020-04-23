import collections
#O(n) time, la complejidad seria la misma al anagrams

def findPerms(string, pattern):
    if len(pattern) > len(string):
        return False
    # armamos un contador para ver si tiene el mismo numero de caracteres en el mismo largo

    ventana1 = collections.Counter(string[:len(pattern)])
    ventana2 = collections.Counter(pattern)
    result = []
    if ventana1 == ventana2:
        return True
    #inicializamos el valor con el valor siguiente al que se acaba de comparar
    i = len(pattern)
    while i < len(string):
        if string[i] in ventana1:
            ventana1[string[i]] += 1
        else:
            ventana1[string[i]] = 1

        ventana1[string[i - len(pattern)]] -= 1
        #movemos la ventana

        if ventana1[string[i - len(pattern)]] == 0:
            del ventana1[string[i - len(pattern)]]
        #si es anagrama, se appendea el indice a una lista de ints a ser retornada
        if ventana1 == ventana2:
            return True
        i += 1
    return result