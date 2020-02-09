import random
A=list()
Estratti=[]
Estratti.append("Venezia")
print (Estratti)
i=0
while i<10:
    A.append(i+1)
    i=i+1
print ("I numeri scelti sono ",A)
i=0
while i<5:
    x=random.randint(0,9-i)
    print ("L'indice scelto è ",x)
    print ("Il numero scelto è ",A[x])
    Estratti.append(A[x])
    A.pop(x)
    i=i+1
    print (A)
print (Estratti)
