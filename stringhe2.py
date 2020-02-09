#gestione stringhe
#menu
parola=input("Inserisci la parola: ")
print("-----------------------------------")
print("1-sottostringa")#s
print("2-divisione di una stringa")#t
print("3-trasforma una stringa in liste")
print("4-cerca un carattere")
print("-----------------------------------")
print("")

lunghezza=len(parola)

i=0
while i<lunghezza:
    print("All'indice ",i, " c'è la lettera ",parola[i])
    i=i+1

print("")
s=int(input("Scegliere cosa fare: "))

if s==1:
    i1=int(input("Inserisci il primo indice: "))
    while i1<0 or i1>lunghezza-1:
        i1=int(input("Inserisci il primo indice: "))
        
    i2=int(input("Inserisci il secondo indice: "))
    while i2<i1 or i2>lunghezza-1:
        i2=int(input("Inserisci il secondo indice: "))

    print("La sottostringa è :",parola[i1:i2+1])

elif s==2:
    t=int(input("Inserisci l'indice di taglio: "))
    while t<0 or t>lunghezza-1:
        t=int(input("Inserisci l'indice di taglio: "))
    print("La prima parola è ",parola[:t])
    print("La seconda parola è ",parola[t:])

elif s==3:
    p1=input("Inserire una frase: ")
    print(p1.split(" "))

elif s==4:
    q=input("Inserisci carattere da cercare: ")
    print("Ho trovato la lettera ",s.find(carattere))
