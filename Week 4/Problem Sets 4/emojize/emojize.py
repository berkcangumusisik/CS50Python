"""
Emoji yazmak metin kadar kolay olmadığından, en azından dizüstü ve masaüstü bilgisayarlarda, bazı programlar, örneğin :thumbs_up:otomatik olarak 👍'ya dönüştürülecek olan yazabileceğiniz "kodları" destekler. Bazı programlar ayrıca takma adları destekler, böylece daha kısa ve öz bir şekilde yazabilirsiniz, örneğin :thumbsup:otomatik olarak 👍'ya dönüştürülecek olan .

Diğer adlara sahip kodların listesi için carpedm20.github.io/emoji/all.html?enableList=enable_list_alias adresine bakın .

adlı bir dosyada , kullanıcıdan İngilizce olarak a'yı isteyen ve ardından bunun "emojize edilmiş" sürümünü çıkaran emojize.pybir program uygulayın ve buradaki tüm kodları (veya takma adları) karşılık gelen emojiye dönüştürün.
"""

import emoji

answer = input("Input : ")
output = emoji.emojize(answer)
print("Output:",output)