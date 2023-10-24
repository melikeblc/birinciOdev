#soru-4 Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
#Alan = pi * r * r
#Çevre = pi * 2 * r 

yariCap = float(input("Dairenin yarıçapını girin : "))

piSayisi = float(3.14) 

daireAlani = piSayisi * yariCap * yariCap 
daireCevre = piSayisi * 2 * yariCap

print("Dairenin alanı : " , daireAlani)
print("Dairenin çevresi : ", daireCevre)