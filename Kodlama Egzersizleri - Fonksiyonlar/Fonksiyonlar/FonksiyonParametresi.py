print("Manava Hoşgeldiniz")

def muhasebe(meyve_ismi):
    kilo = int(input("Lütfen kaç kilo istediğinizi girin:"))
    tutar = kilo * 5
    print(kilo, "kilo", meyve_ismi, "Ödemeniz Gereken Tutar:", tutar)

meyve = input("Lütfen İstediğiniz Meyveyi Girin(Kilosu 5 TL):")



if(meyve=="elma"):
    muhasebe(meyve)
elif(meyve=="armut"):
    muhasebe(meyve)
elif(meyve=="portakal"):
    muhasebe(meyve)
else:
    print("Malesef Elimizde Bu Meyve Yok!")