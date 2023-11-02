#İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

# 1 1 2 3 5 8 13 21 34
fibanocciSeri =[1,1]
#for i in range(18):
while len(fibanocciSeri)<20:        #len, 20'ye kadar fibonacci serisinin kaç eleman içerdiğini gösterir
    yeniSayi= fibanocciSeri[-1]+fibanocciSeri[-2]
    fibanocciSeri.append(yeniSayi)  #oluşan bu yenisayıyı fibonacciseriye ekle.
print(fibanocciSeri)