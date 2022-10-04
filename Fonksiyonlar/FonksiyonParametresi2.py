def odaAlan(x,y):
    print("Oda Alanı:", (x+y)*2)

kisa_kenar1 = int(input("Lütfen birinci odanın kısa kenarı girin:"))
uzun_kenar1 = int(input("Lütfen birinci odanın uzun kenarı girin:"))

kisa_kenar2 = int(input("Lütfen ikinci odanın kısa kenarı girin:"))
uzun_kenar2 = int(input("Lütfen ikinci odanın uzun kenarı girin:"))


oda1 = odaAlan(kisa_kenar1,uzun_kenar1)
oda2 = odaAlan(kisa_kenar2,uzun_kenar2)


print("Evinizin Metrekaresi:", oda1+oda2)



