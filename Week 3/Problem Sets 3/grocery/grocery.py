"""
Alışveriş listesi
Bakkaldan almanız gerekenlerin bir listesini yapma alışkanlığınız olduğunu varsayalım.

adlı bir dosyada grocery.py, kullanıcı kontrol-d'yi girene kadar (bir programa girişini sonlandırmanın yaygın bir yoludur) kullanıcıdan satır başına bir öğe isteyen bir program uygulayın. Ardından, kullanıcının alışveriş listesini, öğeye göre alfabetik olarak sıralanmış ve her satırın önüne kullanıcının o öğeyi girme sayısı ekleyerek büyük harflerle çıktı alın. Öğeleri çoğullaştırmaya gerek yok. Kullanıcının girişini büyük/küçük harfe duyarsız olarak ele alın.
"""
liste = {}

while True:
    try:
        user = input().lower()
        if user  in liste:
            liste[user] += 1
        else:
            liste[user] = 1
    except EOFError:

        for key in sorted(liste.keys()):
            print(f"{liste[key]} {key.upper()}")
        break