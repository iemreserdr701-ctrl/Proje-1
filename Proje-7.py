notlar_listesi = []
print("---Dijital Not Analiz Sistemine Hoşgeldiniz---")
print("Not girmeyi bitirmek için 'bitti' yazın.\n")
while True:
    girdi = input("Öğrenci sınav notunu giriniz:  ").lower()

    if girdi == "bitti" or girdi == "bıttı":
        break
    sinav_notu = int(girdi)
    notlar_listesi.append(sinav_notu)
    print(f"-> {sinav_notu} sisteme kaydedildi.")
print("\n=== SINIF ANALIZ RAPORU ===")
if len(notlar_listesi) > 0:
    print("Girilen Notlar: ", end="" )
    for not_degeri in notlar_listesi:
        print(f"{not_degeri} ", end="")
    print()
    toplam_ogrenci = len(notlar_listesi)
    en_yuksek = max(notlar_listesi)
    en_dusuk = min(notlar_listesi)
    sinif_ortalamasi = sum(notlar_listesi) / toplam_ogrenci

    print(f"Sınıftaki Toplam Öğrenci: {toplam_ogrenci}")
    print(f"SInıf Ortalaması: {sinif_ortalamasi:.2f}")
    print(f"En Yüksek Not: {en_yuksek}")
    print(f"En Düşük Not: {en_dusuk}")
else:
    print("Hiç not girilmediği için analiz yapılmadı")