#cifrario di vigenere
#tabella ascii le lettere sono da 65 a 90
testo=str(input("Inserisci una parola: "))
chiave='augusto'
L=len(testo)
Lc=len(chiave)
q=L//Lc
r=L%Lc
#print(q)
#print(r)
#qq=L/Lc
#print(qq)
chiaverip=""
for i in range(q):
    chiaverip=chiaverip+chiave
print(chiaverip+chiave[0:r])
chiaverip=chiaverip+chiave[0:r]
print(chiaverip)

i=0
while i<L:
    print(ord(testo[i]))
    i=i+1

print("")
 
i=0
while i<L:
    print(ord(chiaverip[i]))
    i=i+1
print("")
i=0
while i<L:
    x=ord(testo[i])+ord(chiaverip[i])
    while(x>90):
      x=x-26
    print(chr(x))
    i=i+1
