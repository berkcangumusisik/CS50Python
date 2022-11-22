"""
Mesajlaşırken veya tweet atarken, zamandan veya yerden tasarruf etmek için sözcükleri kısaltmak alışılmadık bir durum değildir, tıpkı Twitter'ın başlangıçta twttr olarak adlandırılması gibi, ünlüleri atlayarak . adlı bir dosyada , kullanıcıdan bir metnin çıktısını alan ve ardından aynı metni, ister büyük ister küçük harfle girilmiş olsun, tüm sesli harfler (A, E, I, O ve U) çıkarılmış olarak twttr.pyçıkaran bir program uygulayın .str
"""
answer = input("Input : ")
print("Output : ", end = "")
for letter in answer:
    if not letter in ["a","e","i","o","u","A","E","I","O","U"]:
        print(letter, end="")
print()