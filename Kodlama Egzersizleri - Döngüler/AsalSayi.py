

sayi = int(input("Lütfen Bir Sayı Giriniz: "))

sayac = 0

for i in range(2,sayi):
      if (sayi%i==0):
            sayac = 1
            break

if(sayac==1):
      print("Asal Sayı Değil")

else:
      print("Asal Sayı")