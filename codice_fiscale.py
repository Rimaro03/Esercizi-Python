print("CALCOLO CODICE FISCALE")
co=str(input("Inserire il cognome: "))
no=str(input("Inserire il nome: "))
print()
gg=int(input("Inserire il giorno di nascita: "))
mm=str(input("Inserire il mese di nascita: "))
aa=int(input("Inserire l'anno di nascita: "))
print()
#ms=str(input("Sei maschio o femmina? "))
#na=str(input("Scrivi il paese di nascita: "))

#cognome
con=""
f1=""
c=len(co)
i=0
while i<c:
  if(co[i:i+1]!='a' and co[i:i+1]!='e' and co[i:i+1]!='i' and co[i:i+1]!='o' and co[i:i+1]!='u'):
    con=con+co[i]
  i=i+1

i=0
while i<3:
    f1=f1+con[i:i+1]
    i=i+1
print(f1)

#nome
f2=""
con2=""
c=len(no)
i=0
while i<c:
  if(no[i:i+1]!='a' and no[i:i+1]!='e' and no[i:i+1]!='i' and no[i:i+1]!='o' and no[i:i+1]!='u'):
    con2=con2+no[i]
  i=i+1

i=0
while i<4:
    if(i==1):
        z=0
    else:
        f2=f2+con2[i:i+1]
    i=i+1
print(f2)

#anno di nascita
if(aa>=2000 and aa<2010):
    f3='0'
    f3=f3+(str(aa-2000))
elif(aa<2000):
    f3=""
    f3=fr+(str(aa-1900))
else:
    f3=""
    f3=f3+(str(aa-200))
print(f3)

#mese di nascita
f4=""
if mm=="gennaio":
    f4=f4+'A'
elif mm=="febbraio":
    f4=f4+'B'
elif mm=="marzo":
    f4=f4+'C'
elif mm=="aprile":
    f4=f4+'D'
elif mm=="maggio":
    f4=f4+'E'
elif mm=="giugno":
    f4=f4+'H'
elif mm=="luglio":
    f4=f4+'L'
elif mm=="agosto":
    f4=f4+'M'
elif mm=="settembre":
    f4=f4+'P'
elif mm=="ottobre":
    f4=f4+'R'
elif mm=="novembre":
    f4=f4+'S'
elif mm=="dicembre":
    f4=f4+'T'
print(f4)

#giorno di nascita
f5=""
if gg<10:
    f5=f5+'0'+str(gg)
else:
    f5=f5+str(gg)
print(f5)

#codice comune
f6='F964'

#carattere di controllo
f7='U'

#fine
f8=""
f8=f1+f2+f3+f4+f5+f6+f7
print("Il tuo codice fiscale sicuro al 99% è ", f8.upper())
