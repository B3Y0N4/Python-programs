# format() metodunu kullanarak aşağıdaki dilekçe örneğini kullanıcıdan aldığınız verileri ile tamamlayın.
dilikce = ("""TIP FAKÜLTESİ DEKANLIĞINA İSTANBUL {}/{}/{}

Konu:{}

Gereğinin yapılmasını arz ederim.
Saygılarımla,

Ad-Soyad:{}

Adres Bilgileri:{} 									
                                                
Telefon:{}
""")

tarih_gunu = input("Tarihi Günü Giriniz: ")
tarih_ayi = input("Tarihi Ayi Giriniz: ")
tarih_yili = input("Tarihi Yili Giriniz: ")
konu = input("Dilelçenin Konuğu Giriniz: ")
ad_soyad = input("Adinizi ve Soyadinizi Giriniz: ")
adress = input("Adres Bilgilerinizi Giriniz: ")
tel_no = input("Telephone Numaranizi Giriniz: ")

print (dilikce.format(tarih_gunu,tarih_ayi,tarih_yili,konu,ad_soyad,adress,tel_no))
