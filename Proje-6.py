sepet = []
print("--- Akıllı Alışveriş Sepetine Hoşgeldiniz ---")
print("Ekleme yapmayı bitirmek için 'bitti' yazmanız yeterli.\n")
while True:
    urun = input("Sepete eklenecek ürünü yazın: ").lower()
    if urun == "bitti":
        break
    sepet.append(urun)
    print(f"-> {urun} sepete eklendi !")
print("\n---Alışveriniz Tamamlandı!---")
print(f"Sepetinizdeki tüm ürünler: {sepet}")
