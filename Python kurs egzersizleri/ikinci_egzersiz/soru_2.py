# Sözlükleri kullanarak bir şirket çalışanları indeksi oluşturun. Bu isim indeksinde kişilerin isimleri key, 
# kişilerin şu bilgileri de value olmalı: memleket, yaş, görev. Burada kullanacağımız value liste olmalı. 
# Daha sonra bir isim sorgulama ekranı gibi kullanıcıya kimin bilgilerini görüntülemek istediğini sorun ve 
# sorgulanan kişinin ekranda gösterilmesini sağlayın. 
# Proje sonunda elde edeceğiniz çıktı şu şekilde olmalı:
#Lütfen bilgilerini görüntülemek istediğiniz çalışanın ismini girin: Mehmet Yağız
#Mehmet Yağız= Memleket: Adana Yaş: 40 Görev: Direktör
#sozluk_value = {1:{"TL":"Türkiye"}}

sirket_calisanlari = {"Abduljalal" : {"Görev" : "CEO", "Yas" : 18, "Memleket" : "Nijerya"},
                      "Oussama" : {"Görev" : "Müdür", "Yas" : 21, "Memleket" : "Cezayir"},
                      "Ammar" : {"Görev" : "Müdür-Yardimcisi", "Yas" : 18, "Memleket" : "Endonesya"},
                      "Sidqy Walios" : {"Görev" : "Doctor", "Yas" : 19, "Memleket" : "Endonesya"}
}
isim = input("Lütfen bilgilerini görüntülemek istediğiniz çalışanın ismini girin: ")
print (f"{isim} = {sirket_calisanlari[isim]}")