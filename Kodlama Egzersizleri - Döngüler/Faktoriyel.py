print("Faktöriyel Hesaplama Programına Hoşgeldiniz")

sayi = int(input("Lütfen Faktöriyelini Hesaplamak İstediğiniz Sayıyı Girin: "))

faktoriyel = 1

for i in range(2,sayi+1):
    faktoriyel *= i
    print("i değeri:", i)
    print("faktöriyel değeri:", faktoriyel)

print(sayi, "sayısının faktöriyeli şu sayıdır: ", faktoriyel)


