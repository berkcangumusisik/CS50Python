"""
Felipe'nin Taqueria'sı
Harvard Meydanı'nda yemek yenebilecek en popüler yerlerden biri , Felipe's Taqueria'dır ve burada her bir anahtarın değeri dolar cinsinden bir fiyattır ve aşağıda belirtilen mezelerden oluşan bir menü sunar :dict

{
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
adlı bir dosyada taqueria.py, kullanıcının bir sipariş vermesini sağlayan, kullanıcıdan kontrol-d'yi girene kadar (bir programa girişini sonlandırmanın yaygın bir yolu olan) her satıra bir öğe istenmesini sağlayan bir program uygulayın. Girilen her bir kalemden sonra, o ana kadar girilen tüm kalemlerin toplam maliyetini, önüne bir dolar işareti ( $) koyarak ve iki ondalık basamak olarak biçimlendirilmiş olarak görüntüleyin. Kullanıcının giriş durumunu duyarsızca ele alın. Öğe olmayan herhangi bir girişi yok sayın. Menüdeki her öğenin başlık olarak yazılacağını varsayalım .
"""

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True:
    try:
        item = input("Item: ").lower().title()
        if item not in menu:
            raise Exception
    except EOFError:
        break
    except:
        continue
    else:
        total += menu[item]
        print(f'Total :${total:.2f}')
