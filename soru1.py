#Soru 1 - Vücut Kitle İndeksi hesaplama 
#VKİ = kg / m*m

boy = float(input("Lütfen boyunuzu metre cinsinden giriniz : "))
agirlik = float(input("Lütfen kilonuzu kg cinsinden giriniz : "))

vki = agirlik / (boy * boy)

print("Vücut kitle endeksiniz: ", vki )