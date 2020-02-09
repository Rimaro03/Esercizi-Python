s=0
while s==0:
    print("----------------------")
    print("3 lati-triangolo")
    print("4 lati-quadrato")
    print("5 lati-pentagono")
    print("6 lati-esagono")
    print("7 lati-ettagono")
    print("8 lati-ottagono")
    print("9 lati-ennagono")
    print("10 lati-decagono")
    print("----------------------")
    a=int(input("Inserisci il numero di lati: "))
    b=int(input("Inserire la lunghezza dei lati: "))

    if a==3:
        p=a*b
        print("Il perimetro è ", p)
        ap = 0.28867*b
        ar=(p/2)*ap
        print("L'area è ", ar)

    elif a==4:
        p=a*b
        print("Il perimetro è ", p)
        ap = 0.5*b
        ar=(p/2)*ap
        print("L'area è ", ar)

    elif a==5:
        p=a*b
        print("Il perimetro è ", p)
        ap = 0.68819*b
        ar=(p/2)*ap
        print("L'area è ", ar)

    elif a==6:
        p=a*b
        print("Il perimetro è ", p)
        ap = 0.86602*b
        ar=(p/2)*ap
        print("L'area è ", ar)

    elif a==7:
        p=a*b
        print("Il perimetro è ", p)
        ap = 1.03826*b
        ar=(p/2)*ap
        print("L'area è ", ar)

    elif a==8:
        p=a*b
        print("Il perimetro è ", p)
        ap = 1.20710*b
        ar=(p/2)*ap
        print("L'area è ", ar)

    elif a==9:
        p=a*b
        print("Il perimetro è ", p)
        ap = 1.37373*b
        ar=(p/2)*ap
        print("L'area è ", ar)

    else:
        p=a*b
        print("Il perimetro è ", p)
        ap = 1.53884*b
        ar=(p/2)*ap
        print("L'area è ", ar)

    s=int(input("Premere 0 per continuare o 1 per uscire"))
    
