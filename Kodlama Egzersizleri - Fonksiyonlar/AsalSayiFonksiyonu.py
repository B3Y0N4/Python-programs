def asal_sayi(sayi):
    sayac=0
    for i in range(2,sayi):
        if(sayi%i==0):
            print("Asal Sayı Değil")
            sayac = 1
            break
    if(sayac==0):
        print("Sayı Asal")

print("***Asal Sayı Hesaplama Programına Hoşgeldiniz***")

while True:
    sayi = int(input("Lütfen Bir Sayı Giriniz:"))

    asal_sayi(sayi)