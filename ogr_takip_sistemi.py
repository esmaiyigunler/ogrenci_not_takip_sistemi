ogrenci_isimleri = ["Ali", "Ayşe", "Mehmet", "Elif"]  # Öğrenci isimlerini saklayan liste
ogrenci_notlari = [75, 60, 45, 90]                    # Öğrenci notlarını saklayan liste

gecenler = []  # Dersten geçen öğrencilerin isimlerini saklayan liste
kalanlar = []  # Dersten kalan öğrencilerin isimlerini saklayan liste

while True:
    print("Menü:")
    print("1. Öğrenci ismi ve notu eklemek")
    print("2. Öğrencilerin isim ve notlarını görüntülemek")
    print("3. Geçen ve kalan öğrencileri görüntülemek")
    print("4. Çıkış")

    secim = int(input("Lütfen yapmak istediğiniz işlemi seçiniz (1-4): "))

    if secim == 1:
        # Yeni öğrenci ekleme
        ogrenci = input("Eklemek istediğiniz öğrencinin adını giriniz: ")
        not1 = int(input("Eklemek istediğiniz öğrencinin notunu giriniz: "))
        ogrenci_isimleri.append(ogrenci)
        ogrenci_notlari.append(not1)
        print(f"{ogrenci} isimli öğrenci {not1} notuyla listeye eklendi.")

    elif secim == 2:
        # Öğrenci isim ve notlarını görüntüleme
        print("Öğrencilerin İsimleri ve Notları:")
        for i in range(len(ogrenci_isimleri)):
            isim = ogrenci_isimleri[i]
            notu = ogrenci_notlari[i]
            print(isim,notu)

    elif secim == 3:
        # Geçen ve kalan öğrencileri görüntüleme
        gecenler.clear()  # Listeleri her seferinde temizliyoruz ki tekrar ekleme olmasın
        kalanlar.clear()
        
        for i in range(len(ogrenci_isimleri)):
            isim = ogrenci_isimleri[i]
            notu = ogrenci_notlari[i]
            if notu >= 50:
                gecenler.append(isim)
            else:
                kalanlar.append(isim)
        
        print("Dersten Geçen Öğrenciler:")
        if len(gecenler) == 0:
            print("Hiçbir öğrenci dersten geçemedi.")
        else:
            for ogrenci in gecenler:
                print(f"- {ogrenci}")
        
        print("Dersten Kalan Öğrenciler:")
        if len(kalanlar) == 0:
            print("Hiçbir öğrenci dersten kalmadı.")
        else:
            for ogrenci in kalanlar:
                print(f"- {ogrenci}")

    elif secim == 4:
        # Programdan çıkış
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim! Lütfen 1 ile 4 arasında bir sayı giriniz.")
