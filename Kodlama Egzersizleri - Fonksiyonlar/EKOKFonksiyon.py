def ekok(a,b):
    i=2
    ekok=1
    while True:
        if(a%i==0 and b%i==0):
            ekok *= i

            a /= i
            b /= i
        elif(a%i==0 and b%i!=0):
            ekok *= i

            a/=i
        elif(a%i!=0 and b%i==0):
            ekok *= i

            b /= i
        else:
            i += 1
        if(a==1 and b==1):
            break
    return ekok

sayi1 = int(input("1. Sayıyı Girin:"))
sayi2 = int(input("2. Sayıyı Girin:"))

print("EKOK:", ekok(sayi1,sayi2))




