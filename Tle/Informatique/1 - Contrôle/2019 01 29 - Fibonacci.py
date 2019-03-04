def fibonacci(n):
    if(n<2):
        return n		# Premiers termes
    else:
        return fibonacci(n-2)+fibonacci(n-1)

i = int(input("Entrez la valeur de n :"))
print("fibonacci(", i, ") = ", fibonacci(i))

# "fibonacci(10) = 55"
