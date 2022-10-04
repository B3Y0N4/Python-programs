# Bir kullanıcıdan bir dairenin çap bilgisini isteyin. Daha sonra bu bilgiyi kullanarak o dairenin çevresini hesaplayan bir program yazın.
#  (Daire Çevresi Formülü: 2 *  π * r)  π sayısı=3.14
daire_capi = int(input("Dairenin Çapini Giriniz: "))
sonuc = (2 * 3.14 * (daire_capi/2))
print (f"İşlemin sonuc == {sonuc}")