p1=int(input("Inserisci la prima parola: "))
p1=int(input("Inserisci la seconda parola: "))
if len(p1)>len(p2):
	print(a," è più grande di ",b)
elif len(p1)<len(p2):
	print(b," è più grande di ",a)
else:
	print(a," è uguale a ",b)