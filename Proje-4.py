import random 
isim = input("Lütfen isminizi yazınız")
selamlar = [
    f"Hoşgeldin {isim}",
    f"Ooo {isim} nabtın ya nerelerdesin",
    f"{isim} göüzümüz yollarda kaldı hoşgeldin"]
secilen_selam = random.choice(selamlar)
print(secilen_selam)
