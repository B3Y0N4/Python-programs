# Kullanıcıdan bir sayı girmesini isteyin ve sayının çift mi yoksa tek mi olduğunu ekrana bastırın.
# (Ekrana 0 yazdırılırsa çift, 1 yazdırılırsa sayı tektir.)
sayi = int(input("Sayi Giriniz: "))
print ("Ekrana 0 yazdırılırsa çift, 1 yazdırılırsa sayı tektir.")
sonuc = sayi % 2
print (sonuc)