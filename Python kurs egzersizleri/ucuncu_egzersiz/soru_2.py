# Bir kullanıcı giriş paneli hazırlayın. Kullanıcı adı ve parolasının doğru olup-olmadığını denetleyin ve buna göre kullanıcıya yazılı mesajlar verin. 
# Program sonunda şu şekilde bir çıktı elde etmiş olmalısınız:
#Kullanıcı adı ve parola doğru olduğunda:
#"Hoşgeldiniz."
#Yanlış olduğunda:
#"Lütfen kullanıcı adınızı ya da parolanızı tekrar kontrol ediniz."
kullanici_adi = "Abduljalal"
kullanici_sifre = "1234"
ad = input("Kullanici Adi Giriniz: ")
sifre = input("Kullanici Şifrenizi Giriniz: ")

if ad != kullanici_adi and sifre != kullanici_sifre:
    print ("Ne kullanici Adiniz Doğru Ne Şifreniz")
elif ad != kullanici_adi:
    print ("Kullanici Adiniz Yanliş!")
elif sifre != kullanici_sifre:
     print ("Kullanici Şifreniz Yanliş!")
elif ad == kullanici_adi and sifre == kullanici_sifre:
    print ("Hoşgeldiniz.")