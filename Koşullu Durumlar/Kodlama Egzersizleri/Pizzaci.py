print("Pizza Fiyatları\n"
      "Küçük: 15 TL\n"
      "Orta: 22 TL\n"
      "Büyük: 30 TL")

pizza_secimi = input("Hangi boy pizza istersiniz:\n"
                     "(Lütfen seçiminizin tamamını küçük harflerle girin)\n"
                     ":")

if(pizza_secimi == "küçük"):
    print("Seçtiğiniz pizza {} boy. Fiyat: 15 TL".format(pizza_secimi))
elif(pizza_secimi == "orta"):
    print("Seçtiğiniz pizza {} boy. Fiyat: 22 TL".format(pizza_secimi))
elif (pizza_secimi == "büyük"):
    print("Seçtiğiniz pizza {} boy. Fiyat: 30 TL".format(pizza_secimi))