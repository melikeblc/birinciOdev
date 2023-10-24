#soru 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
#kullanıcıdan istenilen bilgiler ; 3 adet sayi

sayi1 = float(input("Birinci sayi : "))
sayi2 = float(input("İkinci sayi : "))
sayi3 = float(input("Üçüncü sayi : "))

enBuyuk = max (sayi1, sayi2, sayi3)

print("En büyük sayi : " , enBuyuk)