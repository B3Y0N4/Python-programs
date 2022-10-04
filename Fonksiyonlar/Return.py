def dikdortgenAlan(x,y):
    return (x+y)*2


kisa_kenar1 = int(input("Lütfen İlk Odanın Kısa Kenarını Girin: "))
uzun_kenar1 = int(input("Lütfen İlk Odanın Uzun Kenarını Girin: "))

kisa_kenar2 = int(input("Lütfen İkinci Odanın Kısa Kenarını Girin: "))
uzun_kenar2 = int(input("Lütfen İkinci Odanın Uzun Kenarını Girin: "))

ilk_dikdortgen = dikdortgenAlan(kisa_kenar1,uzun_kenar1)

ikinci_dikdortgen = dikdortgenAlan(kisa_kenar2,kisa_kenar2)



print("Evinizin toplam ölçüsü:", ilk_dikdortgen+ikinci_dikdortgen)