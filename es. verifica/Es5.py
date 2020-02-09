p1="buongiorno a tutti"
p2=""
i=0
while i<len(p1):
	if(p1[i]==" "):
		p2=p2+"32"
	elif(p1[i]=="a"):
		p2=p2+"Z"
	else:
		p2=p2+str(chr(ord(p1[i])-33))
	i=i+1
print(p2)