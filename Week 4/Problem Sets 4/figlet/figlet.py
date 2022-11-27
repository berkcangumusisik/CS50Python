"""
Adını Frank, Ian ve Glen'in mektuplarından alan FIGlet , 1990'ların başından kalma, bir ASCII sanatı biçimi olan sıradan metinden büyük harfler yapmak için kullanılan bir programdır :

 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
FIGlet tarafından desteklenen yazı tipleri arasında figlet.org/examples.html adresindeki yazı tipleri bulunur .

FIGlet o zamandan beri Python'a pyfiglet adlı bir modül olarak taşınmıştır .

adlı bir dosyada figlet.py, aşağıdakileri sağlayan bir program uygulayın:

Sıfır veya iki komut satırı bağımsız değişkeni bekler:
Kullanıcı metni rastgele bir yazı tipinde çıkarmak istiyorsa sıfır.
Kullanıcı belirli bir yazı tipinde metin çıktısı almak isterse iki, bu durumda ikisinden ilki -fveya olmalı --fontve ikisinden ikincisi yazı tipinin adı olmalıdır.
Kullanıcıdan bir strmetin ister.
Bu metni istenen yazı tipinde verir.
Kullanıcı iki komut satırı argümanı sağlarsa ve birincisi -fveya --fontveya ikincisi bir yazı tipinin adı değilse, program sys.exitbir hata mesajı ile çıkış yapmalıdır.
"""

import sys
import random

from pyfiglet import Figlet
figlet = Figlet()

if len(sys.argv) == 1:
    isRandom = True
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    isRandom = False
else:
    print("Invalid usage")
    sys.exit(1)

figlet.getFonts()

if isRandom == False:
    try:
        font = figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

msg = input("Input: ")

output = figlet.renderText(msg)

print("Output: ")
print(output)