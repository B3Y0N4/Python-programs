# Kullanıcıdan, kullanıcı adı ve parola isteyin. Daha sonra kullanıcının kullanıcı adı ve parolasının karakter uzunluğunun 
# toplam 20 karakterden fazla olup-olmadığını denetleyin. 20 karakterden uzun olduğu durumda bir uyarı mesajı verin. 
# Program sonunda elde edeceğiniz çıktı şu şekilde olmalı:
#"Kullanıcı adı ve parolanızın toplam uzunluğu 20 karakteri geçmemeli!"
adi = input("Adinizi giriniz: ")
sifre = input("Şifrenizi Giriniz: ")
toplam = len(adi) + len(sifre)
if toplam > 20:
    print ("Kullanıcı adı ve parolanızın toplam uzunluğu 20 karakteri geçmemeli!")