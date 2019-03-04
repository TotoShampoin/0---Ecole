def factorielle(n):
    if n=0:
        return 1    # 0! = 1
    else:
        return factorielle(n)*factorielle(n-1)


i = int(input("Entrez la valeur de n : "))
print(i, "! = ", factorielle(n), sep = '')

#sep = '' >>> ça donnera "9!" au lieu de "9 !"

