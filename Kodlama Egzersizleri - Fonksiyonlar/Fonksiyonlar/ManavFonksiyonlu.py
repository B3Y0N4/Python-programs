print("Manava Hoşgeldiniz")

def muhasebe():
    kilo = int(input("Lütfen kaç kilo istediğinizi girin:"))
    tutar = kilo * 5
    print("Ödemeniz Gereken Tutar:", tutar)

meyve = input("Lütfen İstediğiniz Meyveyi Girin(Kilosu 5 TL):")



if(meyve=="elma"):
    muhasebe()
elif(meyve=="armut"):
    muhasebe()
elif(meyve=="portakal"):
    muhasebe()
else:
    print("Malesef Elimizde Bu Meyve Yok!")