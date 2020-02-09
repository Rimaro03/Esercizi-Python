#first project
import math
a=int(input("Inserire il primo numero: "))
b=int(input("Inserisci il secondo numero: "))

print("1-addizione")
print("2-sottrazione")
print("3-moltiplicazione")
print("4-divisione")
print("5-radice quadrata")
s=int(input("Scegli un numero: "))

if s==1:
    print("Hai scelto addizione")
    r=a+b
elif s==2:
    print("Hai scelto sottrazione")
    r=a-b
elif s==3:
    print("Hai scelto moltiplicazione")
    r=a*b
elif s==4:
    print("Hai scelto divisione")
    if b==0:
        print("Errore")
    else:
        r=a/b
else:
    if a>=0:
        r=(int)(math.sqrt(a))
    else:
        print("Errore")

                          
print("Il risultato e' ",r)
