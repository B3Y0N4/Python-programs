# Bir AVM'ye ateş ölçer programı yazmalısınız. 
# Kullanıcıya ateşini sorun daha sonra ateşinin derecesine göre AVM'ye girip-giremeyeceğini kullanıcıya belirtin. 
# Program sonunda şöyle bir çıktı elde etmelisiniz:
#"Ateşiniz 39 derece. AVM'ye Giremezsiniz!"
derece = float(input("Vucut issinizi Giriniz Cº: "))
if derece >= 36.4 and derece <= 37.6:
     print(f"Ateşiniz {derece} derece. AVM'ye Girebilirsiniz.")
else:
     print(f"Ateşiniz {derece} derece. AVM'ye Giremezsiniz!")