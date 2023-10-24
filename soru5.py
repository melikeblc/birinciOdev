# Soru5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

# Palindrom sayi, hem sağdan-sola hem soldan-sağa okunduğunda aynı olan sayıdır.

sayi = input("Bir sayı giriniz : ")

tersSayi = sayi[::-1]

if sayi == tersSayi:
    print("Girdiğiniz sayı bir palindrom sayıdır.")
else:
    print("Girdiğiniz sayı palindrom sayı değildir.")
