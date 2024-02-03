#função contador de palavras:
def func_palavs():
    X = input('insira uma frase: ')
    LIS = X.split()
    D = {}
    for i in LIS:
        if i not in D:
            D[i] = 1
        else:
            D[i] = D[i] + 1
    print(D)
func_palavs()

#função contador de letras
def func_lets():
    x = input('insira algo: ')
    d = {}
    for i in x:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    print(d)
func_lets()
    
    
