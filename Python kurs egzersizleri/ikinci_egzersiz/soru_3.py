# 5 öğrenciden oluşan bir öğrenci not sözlüğü oluşturun. Bu sözlükte öğrencilerin notları value olarak bir listede toplansın. 
# Kullanıcıya hangi öğrencinin notlarını görmek istediğini sorun. 
# Öğrencinin notu görüntülendiğinde program sonunda şöyle bir çıktı elde etmelisiniz:
#Lütfen notlarını görmek istediğiniz öğrencinin adını girin: Mehmet
#Mehmet isimli öğrencinin 1.Sınav Notu:72
#                             2.Sınav Notu:66
#                             3.Sınav Notu:48
#Not Ortalaması: 62.0
ogrenci_notlari = {"Abduljalal": [85,96,80], "Ammar": [95,86,70], "Sidqy": [100,94,79],"Oussama": [91,76,92], "Arman": [89,65,100],"osman": [78,83,90]}
ogrenci_adi = input("Lütfen notlarını görmek istediğiniz öğrencinin adını girin: ")
ogrenci_ortalama = (ogrenci_notlari[ogrenci_adi][0] + ogrenci_notlari[ogrenci_adi][1] + ogrenci_notlari[ogrenci_adi][2])/ 3
print (f"{ogrenci_adi} isimli öğrencinin 1.Sınav Notu:{ogrenci_notlari[ogrenci_adi][0]}")
print (f"{ogrenci_adi} isimli öğrencinin 1.Sınav Notu:{ogrenci_notlari[ogrenci_adi][1]}")
print (f"{ogrenci_adi} isimli öğrencinin 1.Sınav Notu:{ogrenci_notlari[ogrenci_adi][2]}")
print (f"{ogrenci_adi} isimli öğrencinin notu ortalamasi {ogrenci_ortalama}")