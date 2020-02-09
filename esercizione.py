import random

a=[]
b=[]
s=[]
m=[]
d=[]
v=[]
v2=[]
c=[]

print("Creazione di due vettori")

i=0
while(i<10):
    x=random.randint(0,30)
    a.append(x)
    i=i+1;
print("Vettore 1: ",a)

i=0
while(i<10):
    x=random.randint(0,30)
    b.append(x)
    i=i+1;
print("Vettore 1: ",b)
s=0
while s==0:
    print("")
    print("1-Somma i componenti dei vettori")
    print("2-Moltiplica un vettore per un numero")
    print("3-Sottrai i componenti dei vettori")
    print("4-Moltiplica i componenti dei vettori, poi sommali")
    print("5-Unisci i due vettori")
    print("6-Media dei numeri di posto pari nel primo vettore")
    print("")
    h=int(input("Scegli l'operazione da effettuare: "))

    if(h==1):
        i=0
        while(i<10):
            s.append(a[i]+b[i])
            i=i+1
        print(s)
    elif(h==2):
        k=int(input("Scegliere il moltiplicatore: "))
        d=int(input("Scegliere il vettore da moltiplicare (1 o 2): "))
        i=0
        while i<10:
            if(d==1):
                m.append(a[i]*k)
            elif(d==2):
                m.append(b[i]*k)
            i=i+1
        print(m)
    elif(h==3):
        i=0
        while(i<10):
            d.append(a[i]-b[i])
            i=i+1
        print(d)
    elif(h==4):
        i=0
        while(i<10):
            v.append(a[i]*b[i])
            i=i+1
        print(v)
        i=0
        v2=0
        while(i<10):
            v2=v2+v[i]
            i=i+1
        print(v2)
    elif(h==5):
        c.append(a+b)
        print(c)
    elif(h==6):
        i=0
        l=0
        while(i<10):
            if(i%2==0):
                l=l+a[i]
            i=i+1
        print(l/5)
    s=int(input("Premere 0 per continuare o 1 per uscire"))
