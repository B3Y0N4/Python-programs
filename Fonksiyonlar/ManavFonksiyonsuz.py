print("Manava Hoşgeldiniz")

meyve = input("Lütfen İstediğiniz Meyveyi Girin(Kilosu 5 TL):")

if(meyve=="elma"):
    kilo = int(input("Lütfen kaç kilo istediğinizi girin:"))
    tutar = kilo*5
    print("Ödemeniz Gereken Tutar:", tutar)
elif(meyve=="armut"):
    kilo = int(input("Lütfen kaç kilo istediğinizi girin:"))
    tutar = kilo * 5
    print("Ödemeniz Gereken Tutar:", tutar)
elif(meyve=="portakal"):
    kilo = int(input("Lütfen kaç kilo istediğinizi girin:"))
    tutar = kilo * 5
    print("Ödemeniz Gereken Tutar:", tutar)
else:
    print("Malesef Elimizde Bu Meyve Yok!")