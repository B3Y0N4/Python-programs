# Sözlükleri Kullanarak Bir Telefon Rehberi Yazın. Bu rehberde kullanıcıya kimin telefonunu görüntülemek istediğini 
# sorun ve kullanıcının girdiği isme göre o kişinin telefon numarasını yazdırın. Proje sonunda elde edeceğiniz çıktı şuna benzer olmalı:
#Lütfen numarasını öğrenmek istediğiniz kişinin adını girin: Ahmet
#Ahmet isimli kişinin numarası şu şekildedir: 0532 862 98 47
telefon_rehberi = {"Amar" :"0552 847 45 96","Samer" : "0552 784 76 21" }
isim = input("Lütfen numarasını öğrenmek istediğiniz kişinin adını girin: ")
print (f"{isim} isimli kişinin numarası şu şekildedir: {telefon_rehberi[isim]}")