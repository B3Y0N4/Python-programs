# Kullanıcıdan bir parola isteyin. Girilen parolanın 3 ile 8 karakter uzunluğunda olup-olmadığını kontrol edin. 
# Aynı zamanda kullanıcının bir parola girdiğinden emin olun. Girilen parola 3 karakterden az ya da 8 karakterden uzun ise ya da 
# kullanıcı hiçbir parola girmemişse kullanıcıya gerekli uyarıları verin. Programınız şartların sağlandığı bir parola belirlenene kadar devam etsin.
# Şartların sağlandığı bir parola belirlendiğinde ise programı break deyimi ile sonlandırın. Program sonunda şöyle bir çıktı elde etmiş olmalısını:
parola = input("Parola belirleyin: ")
while True:
    if len(parola) < 3 or len(parola) > 8:
        print ("parola 8 karakterden uzun 3 karakterden kısa olmamalı !")
        parola = input("Parola belirleyin: ")
    elif len(parola) == 0:
        print ("Boş bir parola giridiniz !")
        parola = input("Lütfen parolanizi tekrar belirleyiniz: ")
    else:
        print ("Paraloniz Belirlendi ")
        break 

