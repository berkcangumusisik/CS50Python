""" 
Matematik Tercümanı
Python , değerleri ve hatta değişkenleri toplamak, çıkarmak, çarpmak veya bölmek için kod yazabileceğiniz matematiği zaten desteklemektedir . Ama kullanıcıların Python'u bilmeden de matematik yapmalarını sağlayan bir program yazalım .

adlı bir dosyada interpreter.py, kullanıcıdan bir aritmetik ifade isteyen ve ardından sonucu bir ondalık basamak olarak biçimlendirilmiş bir kayan nokta değeri olarak hesaplayan ve çıkaran bir program uygulayın. Kullanıcı girişinin ve arasında bir boşluk ve ve arasında bir boşluk olacak şekilde , olarak biçimlendirileceğini varsayalım , x y zburada :xyyz

xbir tamsayıdır
y, +, veya -_*/
zbir tamsayıdır
Örneğin, kullanıcı girdiyse, 1 + 1programınızın çıktısı olmalıdır 2.0. Varsayalım ki, yo /zaman zolmayacak 0.

Unutmayın ki pythonkendisi nasıl Python için bir tercümansa, siz interpreter.pyde matematik için bir tercüman olacaksınız!
"""

answer = input("Expression: ")

x,y,z = answer.split(" ")

a = float(x)
c = float(z)

if y == "+":
    print(a + c)
elif y == "-":
    print(a - c)
elif y == "*":
    print(a * c)
elif y == "/":
    print(a / c)