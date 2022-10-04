# Bir pizzacının fiş hesaplama programını yazın. 
# Kullanıcıya ne tür bir pizza istediğini sorun ve kullanıcının istediği pizza türüne göre ödemesi gereken meblağı kullanıcıya gösterin. 
# Program sonunda elde edeceğiniz çıktı şu şekilde olmalı:
#"Seçiminiz: Orta Boy
#Ödemeniz Gereken Miktar: 22 TL"
#Büyük Boy: 30 TL
#Orta Boy: 22 TL
#Küçük Boy: 15 TL
print ("""
          Büyük Boy için 1
          Orta  Boy için 2
          Küçük Boy için 3 tiklatiniz 
          """)
secim = int(input("Pizza Seçiminiz: "))
if secim == 2:
    print ("Ödemeniz Gereken Miktar: 22 TL")
elif secim == 1:
    print ("Ödemeniz Gereken Miktar: 30 TL")
elif secim == 3:
    print ("Ödemeniz Gereken Miktar: 30 TL")
else :
    print ("Hatali bir giriş yaptiniz")
