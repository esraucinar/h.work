""" Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız. """

sayi= int(input("Sayı giriniz:"))
toplam=0                           #mükemmel sayı, kendisi hariç bölenlerinin toplamı kendisine eşit olduğunda tanımlanır. 
                                #"toplam" değişkeni kendisi hariç bölenlerin toplamını saklar. sıfır yazmamız, başlangıçta hesaplamak için(?)
for i in range(1,sayi):         #bir sayı girildi.mesela 6, 6'ya kadar olan sayıları(yani i)'yi hesaplar. 6'nın 6'ya kadar olan sayılardan kalanı sıfır olanı bulur. 
    if sayi%i==0:               #modu sıfır olanı bulduysaa
        toplam+=i               #toplam değişkenine, her döngüde i'yi ekle.
if (sayi==toplam):              #nihayetinde toplamı bulduktan sonra, girilen sayıya eşitse mükemmel sayıdır.
    print("mükemmel sayıdır.")
else:
    print("mükemmel sayı değildir.")




