import collections

#O(n) time
#complejidad de espacio O(1), siendo del tamano del alfabeto

def findAnagrams(string, pattern):
    length = len(pattern)
    if length > len(string):
        return []
    # armamos un contador para ver si tiene el mismo numero de caracteres en el mismo largo
    
    ventana1 = collections.Counter(string[:length])
    ventana2 = collections.Counter(pattern)
    result = []
    if ventana1 == ventana2:
        result.append(0)
    #inicializamos el valor con el valor siguiente al que se acaba de comparar 
    i = length
    while i < len(string): #loop se corre menos de len(string) veces, que seria O(1)xO(n), lo que seria O(n)
        #todas las operaciones se ejecutan en tiempo constante
        if string[i] in ventana1:
            ventana1[string[i]] += 1
        else:
            ventana1[string[i]] = 1

        ventana1[string[i - length]] -= 1
        #movemos la ventana

        if ventana1[string[i - length]] == 0:
            #si la entrada llega a ser 0, la eliminamos
            del ventana1[string[i - length]]
        #si es anagrama, se appendea el indice a una lista de ints a ser retornada
        if ventana1 == ventana2:
            #tiempo constante
            result.append(i - length + 1)
        i += 1
    return result
