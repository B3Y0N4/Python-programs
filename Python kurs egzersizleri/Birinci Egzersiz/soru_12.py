# Kullanıcının hangi ayda ne kadar doğalgaz faturası ödeyeceğini hesaplayan bir program yazın.
#  İlk olarak hangi ayı hesaplamak istediğini sorun daha sonra o ayda kaç metreküp doğalgaz kullandığını sorun.
#  Daha sonra ekrana "Şu ayda şu kadar fatura ödemeniz gerekiyor." şeklinde bir cümle bastırın. (Doğalgazın metreküp fiyatı: 1.54).
ay= input("Hangi ayin doğal gaz faturanizi ölçmek istersiniz: ")
metre_kup = int(input("Lütfen metrekup doğal gaz kullandinizi giriniz: "))
birim = 1.54
fatura = metre_kup*birim

print (f"{ay} ayinda  ödeyeceğniz doğal gazin faturasi {fatura}dir ")