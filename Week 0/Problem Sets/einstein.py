"""
Fizik okumamış olsanız bile (yakın zamanda veya daha önce!), enerjiyi (Joule cinsinden ölçülür), kütleyi (kilogramla ölçülür) ve ışık hızını (yaklaşık 300000000 metre olarak ölçülür) temsil ettiğini duymuş olabilirsiniz. saniyede), Albert Einstein ve arkadaşlarına göre. Esasen formül, kütle ve enerjinin eşdeğer olduğu anlamına gelir.

einstein.py adlı bir dosyada, Python'da kullanıcıdan kütleyi bir tamsayı (kilogram cinsinden) olarak isteyen ve ardından eşdeğer Joule sayısını bir tamsayı olarak veren bir program uygulayın. Kullanıcının bir tamsayı gireceğini varsayalım.
"""

c = 300000000
m = int(input("m = "))
e = m * (c ** 2)
print(e)