def ebob(a,b):
    i=1
    ebob=1
    while(i <= a and i <= b):
        if(a%i==0 and b%i==0):
            ebob = i
        i += 1
    return ebob

sayi1 = int(input("1. Sayıyı Girin:"))
sayi2 = int(input("2. Sayıyı Girin:"))

print("EBOB:", ebob(sayi1,sayi2))


