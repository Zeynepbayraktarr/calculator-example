print(""""
[1] Toplama İşlemi
[2] Çıkarma İşlemi
[3] Çarpma İşlemi
[4] Bölme İşlemi
[5] Çıkış

""")

giris = input("Seçiminiz  :")


if giris == "1":
    sayi1 = input("Birinci Sayıyı Giriniz : ")
    sayi1 = int(sayi1)
    sayi2 = input("İkinci Sayıyı Giriniz : ")
    sayi2 = int(sayi2)

    print("İşlem Sonucu : ",sayi1 + sayi2)

elif giris == "2":
    sayi1 = input("Birinci Sayıyı Giriniz : ")
    sayi1 = int(sayi1)
    sayi2 = input("İkinci Sayıyı Giriniz : ")
    sayi2 = int(sayi2)

    print("İşlem Sonucu : ", sayi1 - sayi2)

elif giris == "3":
    sayi1 = input("Birinci Sayıyı Giriniz : ")
    sayi1 = int(sayi1)
    sayi2 = input("İkinci Sayıyı Giriniz : ")
    sayi2 = int(sayi2)

    print("İşlem Sonucu : ", sayi1 * sayi2)

elif giris == "4":
    sayi1 = input("Birinci Sayıyı Giriniz : ")
    sayi1 = int(sayi1)
    sayi2 = input("İkinci Sayıyı Giriniz : ")
    sayi2 = int(sayi2)

    print("İşlem Sonucu : ", sayi1 / sayi2)
elif giris == "5":

    print("Çıkış Yapıldı")

elif giris == "q" or "Q":
    print("Çıkılıyor...")
    quit()
else:
    print("Hatalı Girdiniz")



