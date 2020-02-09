s1 = "orol"
t = s1.upper()
n = ""
print (t)
k = 3
for i in t:
  m = ord(i)
  if (m>=65+k) and (m<=90):
    m = m - k 
    car = chr(m)
    if (car == 'W'):
      m = m - k
    elif (car == 'Y'):
      m = m - k
    elif (car == 'X'):
      m = m - k
    elif (car == 'K'):
      m = m - k
    elif (car == 'J'):
      m = m - k
    n = n + chr(m)
  else:
    n = n + chr(m+(26-k))
print (n)
