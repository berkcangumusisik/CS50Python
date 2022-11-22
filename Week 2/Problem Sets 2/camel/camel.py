"""
Bazı dillerde, değişken adları birden çok sözcükten oluştuğunda, ilk sözcüğün ilk harfinin küçük ama sonraki her sözcüğün ilk harfinin büyük olduğu durumlarda, değişken adları için camel case (diğer bir deyişle "karışık durum" olarak da bilinir) kullanılması yaygındır. . Örneğin, bir kullanıcının adı için bir değişken çağrılabilirken name, bir kullanıcının adı için bir değişken çağrılabilir firstNameve bir kullanıcının tercih ettiği ilk isim (örneğin, takma ad) için bir değişken çağrılabilir preferredFirstName.

Python, tersine, tüm harfleri küçük olacak şekilde sözcüklerin alt çizgilerle ( ) ayrıldığı yılan durumunu önerir . Örneğin, aynı değişkenler Python'da sırasıyla , ve olarak adlandırılır._namefirst_namepreferred_first_name

adlı bir dosyada camel.py, kullanıcıdan deve durumunda bir değişkenin adını isteyen ve yılan durumunda karşılık gelen adı çıkaran bir program uygulayın. Kullanıcı girişinin gerçekten deve durumunda olacağını varsayalım.
"""
camelCase = input("camelcase: ")
print("snake_case", end = "")
for letter in camelCase:
    if letter.isupper():
        print("_" + letter.lower() , end = "")
    else:
        print(letter, end="")
print()