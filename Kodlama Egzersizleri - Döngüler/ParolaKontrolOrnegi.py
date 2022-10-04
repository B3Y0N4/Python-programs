print("""Forumumuza Hoşgeldiniz

Lütfen İlk Olarak Parola Belirleyin""")

while True:


    parola = input("Lütfen Parolanızı Giriniz: ")

    if (not parola):
        print("Parola Boş Bırakılamaz!")

    elif(len(parola) in range(3,9)):
        print("Parolanız Başarıyla Oluşturuldu. \n Lütfen Not Alınız:", parola)
        break
    else:
        print("Parola 3 ile 8 karakter uzunluğunda olmalı!")

