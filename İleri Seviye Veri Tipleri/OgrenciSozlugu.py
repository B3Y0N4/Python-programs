ogrenciler = {"Ahmet": [80,85,83],
              "Ayşe": [77,95,63],
              "Mehmet": [65,52,49],
              "Sude": [92,97,99]}

kisi = input("Lütfen notlarını görüntülemek istediğiniz öğrencinin adını girin: ")

print("""{} isimli öğrencinin 1. Sınav Notu: {}
                                2. Sınav Notu: {}
                                3. Sınav Notu: {}
Not Ortalaması: {}""".format(kisi, ogrenciler[kisi][0],
                             ogrenciler[kisi][1],
                             ogrenciler[kisi][2],
                             (ogrenciler[kisi][0]+ogrenciler[kisi][1]+ogrenciler[kisi][2])/3))