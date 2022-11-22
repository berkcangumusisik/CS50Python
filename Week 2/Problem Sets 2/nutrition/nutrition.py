"""
ABD Gıda ve İlaç İdaresi (FDA), "Amerika Birleşik Devletleri'nde en sık tüketilen 20 çiğ meyvenin beslenme bilgilerini gösteren" indirilebilir/basılabilir posterler sunmaktadır. Perakende satış mağazaları posterleri indirebilir, yazdırabilir, sergileyebilir ve/veya mağazalardaki ilgili yiyeceklerin yakınında tüketicilere dağıtabilir.”

adlı bir dosyada , tüketicilerden bir meyveyi (büyük/küçük harfe duyarsız olarak) girmelerini isteyen ve ardından FDA'nın meyveler için metin olarak da bulunan posterinenutrition.py göre o meyvenin bir porsiyonundaki kalori sayısını veren bir program uygulayın . Büyük harf kullanımı bir yana, kullanıcıların meyveleri tam olarak posterde yazıldığı gibi gireceğini varsayalım (örneğin, , değil ). Meyve olmayan herhangi bir girdiyi yok sayın.strawberriesstrawberry

İpuçları
Her meyve için bir tane olmak üzere 20 Boole ifadesine sahip bir koşullu kullanmak yerine, dictbir meyveyi kalorileriyle ilişkilendirmek için bir kullanmak daha iyidir!
kis a strve dis a ise , aşağıdaki gibi bir kodla bir anahtar dictolup olmadığını kontrol edebilirsiniz :kd
if k in d:
    ...
Kalorisini yağdan değil, meyvenin kalorisinden çıkarmaya özen gösterin!
"""

fruits = [
    {"fruit":"apple", "calories":130},
    {"fruit":"avocado", "calories":50},
    {"fruit":"banana", "calories":110},
    {"fruit":"cantaloupe", "calories": 50},
    {"fruit":"grapefruit", "calories": 60},
    {"fruit":"grapes", "calories": 90},
    {"fruit":"honeydew melon", "calories": 50},
    {"fruit":"kiwifruit", "calories": 90},
    {"fruit":"lemon", "calories": 15},
    {"fruit":"lime", "calories": 20},
    {"fruit":"nectarine", "calories": 60},
    {"fruit":"orange", "calories": 80},
    {"fruit":"peach", "calories": 60},
    {"fruit":"pear", "calories": 100},
    {"fruit":"pineapple", "calories": 50},
    {"fruit":"plums", "calories": 70},
    {"fruit":"strawberries", "calories": 50},
    {"fruit":"sweet cherries", "calories": 100},
    {"fruit":"tangerine", "calories": 50},
    {"fruit":"watermelon", "calories": 80}
]

text = input("Item: ")

for x in fruits:
    fruit = x['fruit']
    calories = x['calories']

    if text.lower() == fruit:
        print("Calories: " + str(calories))