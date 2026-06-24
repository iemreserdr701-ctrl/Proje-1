tur_sayisi = 1

while tur_sayisi < 4:
    isim = input("Lütfen İsminizi yazınız: ")
    
    if tur_sayisi == 1:
        print(f"Hoş geldin {isim}")
    elif tur_sayisi == 2: 
        print(f"Ooo {isim} yine mi sen?")
    elif tur_sayisi == 3:
        print(f"Yeter lao {isim} her yerdde sen haooo")
    
    # DİKKAT: Bu satırın başında tam 4 boşluk var. 
    # Yani if/elif'lerin İÇİNDE DEĞİL, tamamen altındadır!
    tur_sayisi = tur_sayisi + 1

print("Program bitti, pc kaçtı gg g.o")