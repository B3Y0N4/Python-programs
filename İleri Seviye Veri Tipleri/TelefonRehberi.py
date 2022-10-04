telefon_rehberi = {"Ahmet": "0532 862 97 84",
                   "Mehmet": "0533 862 98 47",
                   "Ayşe": "0545 412 56 960",
                   "Sude": "0531 896 47 85"}

kisi = input("Lütfen numarasını öğrenmek istediğiniz kişinin ismini girin: ")

print("{} isimli kişinin telefon numarası şu şekildedir: {}".format(kisi, telefon_rehberi[kisi]))
