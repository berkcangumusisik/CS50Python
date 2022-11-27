"""
1 ile 100 arasında bir sayı düşünüyorum...

Bu ne?
adlı bir dosyada game.py, aşağıdakileri sağlayan bir program uygulayın:

Kullanıcıdan bir seviye ister,. Kullanıcı pozitif bir tamsayı girmezse, program tekrar sormalıdır.
Rastgele 1 ile arasında bir tamsayı üretir., dahil, randommodülü kullanarak.
Kullanıcıdan bu tamsayıyı tahmin etmesini ister. Tahmin pozitif bir tamsayı değilse, program kullanıcıyı tekrar sormalıdır.
Tahmin bu tamsayıdan küçükse, program çıktı almalı Too small!ve kullanıcıyı tekrar uyarmalıdır.
Tahmin bu tamsayıdan büyükse, program çıktı almalı Too large!ve kullanıcıyı tekrar uyarmalıdır.
Tahmin edilen tamsayı ile aynı ise, program çıktı almalı Just right!ve çıkmalıdır.
"""
import random

while True:
    try:
        level = int(input("Level : "))
        if level > 0:
            break
    except:
        pass

number = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess : "))
        if guess > 0:
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
        pass