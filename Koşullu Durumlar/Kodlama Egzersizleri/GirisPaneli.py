kullanici_adi_veritabani = "Bilal"
kullanici_password_veritabani = "12345"


kullanici_adi = input("Lütfen kullanıcı adını girin: ")
kullanici_password = input("Lütfen şifrenizi girin: ")

if(kullanici_adi == kullanici_adi_veritabani and kullanici_password == kullanici_password_veritabani):
    print("Hoşgeldiniz {}".format(kullanici_adi))
else:
    print("Kullanıcı adı ya da parola hatalı!")