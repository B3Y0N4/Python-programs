calisanlar = {"Mehmet Yağız": ["İstanbul", 40, "Direktör"],
              "Ahmet Tozkoparan": ["Ankara", 39, "Genel Müdür"],
              "Ayşe Gündüz": ["Samsun", 42, "Departman Müdürü"]}

kisi = input("Lütfen bilgilerini görmek istediğiniz çalışanın ismini girin: ")

print("{} = Memleket: {} Yaş: {} Görev: {}".format(kisi, calisanlar[kisi][0],
                                                   calisanlar[kisi][1],calisanlar[kisi][2]))

