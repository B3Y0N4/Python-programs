kullanici_adi = input("Lütfen bir kullanıcı adı girin: ")
password = input("Lütfen bir şifre girin: ")


if(len(kullanici_adi)+len(password) > 20):
    print("Kullanıcı adı ve parolanın karakter uzunluğu 20 karakteri geçmemeli!")
else:
    print("Kullanıcı kaydı başarılı.")