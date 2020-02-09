#CIFRAGGIO DI AUGUSTO
#la lunghezza della chiave non deve superare la lunghezza della parola chiara esempio:
#buongiorno
#ciaociaoci
#bisogna eseguire la somma della lettera sopra con quella sotto e fare la differenza di 26 finchè non rientra tra 65-90

#inserire testo in chiaro
testo_chiaro = str(input("Inserisci testo senza spazi di lunghezza superiore a 7: ")).upper()
testo_in_chiaro = testo_chiaro.replace(" ","")
chiave = str(input("Inserisci chiave: ")).upper()
while len(chiave)>len(testo_in_chiaro):
    chiave = str(input("Re-inserisci chiave: ")).upper()
lt = len(testo_in_chiaro)
lc = len(chiave)
q = lt//lc
r = lt%lc
#print ("Quoto intero ",q)
#print ("Resto ",r)
#senza doppie barre la divisione non è intera esempio:
#qq = lt/lc oppure si può scrivere q = int(lt/c) e restituisce un intero
#print ("Quoto reale ",qq)
chiave_rip = ""
for i in range(q):
    chiave_rip = chiave_rip + chiave
#print (chiave_rip)
chiaverip = chiave_rip + chiave[0:r]
print (chiaverip)
#per il momento stampare gli ordinali del testo in chiaro e stampare gli ordinali della chiave_rip
for i in range(lt):
    print (ord(testo_in_chiaro[i]) - 64,end = " ")
print ()
for i in range(lt):
    print (ord(chiaverip[i]) - 64,end = " ")
print ()
cifrato = ""
for i in range(lt):
    x = (ord(chiaverip[i]) - 64) - (ord(testo_in_chiaro[i]) - 64)
    if x>0:
      cifrato = cifrato + str(x)
    else:
      x = x + 26
      cifrato = cifrato + str(x)
print (cifrato)

