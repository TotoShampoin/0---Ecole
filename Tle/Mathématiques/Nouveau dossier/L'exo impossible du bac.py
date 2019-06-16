import math

p = int(input("p = "))

n = 0
u = 1.

print()

while u>=10**(-p):
    print("u("+str(n)+") = "+str(u))
    n += 1
    u = u-math.log(1+u)

print("\nu("+str(n)+") = "+str(u))

