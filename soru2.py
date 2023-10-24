#Soru - 2 Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

# kullanıcıdan istenecek bilgiler ; maaş bilgisi, zam oranı 
# kurulacak denklemler ; zam miktarı, zamlı maaş 

maas = float(input("Lütfen güncel maaşınızı giriniz : "))
zamOrani = float(input("Lütfen zam oranınızı giriniz : "))

#zam miktarı hesaplama

zamMiktari = maas * (zamOrani / 100)

#zamlı maaş hesaplama = maas + zamMiktari

zamliMaas = maas + zamMiktari 

print("Yeni zamlı maaşınız : " , zamliMaas)
