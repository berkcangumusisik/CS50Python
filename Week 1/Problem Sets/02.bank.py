""" 
Ana Sayfa Federal Tasarruf Bankası
Seinfeld'in 7. sezonun 24. bölümünde Kramer , " merhaba" ile karşılanmayan herkese 100 dolar vermeyi vaat eden bir bankayı ziyaret eder. Kramer bunun yerine bir "merhaba" ile karşılanır ve bunun "merhaba" olmadığı konusunda ısrar eder ve bu nedenle 100 dolar ister. Bankanın müdürü bir uzlaşma önerir: "'H' ile başlayan bir selamlamanız var, 20 dolar kulağa nasıl geliyor?" Kramer kabul eder.

adlı bir dosyada bank.py, kullanıcıdan bir selamlama isteyen bir program uygulayın. Karşılama "merhaba" ile başlıyorsa, çıktı $0. Karşılama bir "h" ile başlıyorsa ("merhaba" değil), çıktı $20. Aksi takdirde, çıktı $100. Kullanıcının selamlamasında önde gelen boşlukları yok sayın ve kullanıcının selamlamasını büyük/küçük harfe duyarsız olarak ele alın.
"""
answer = input("Greeting : ")
if "hello" in answer.lower():
    print("$0")
elif "h" == answer.lower()[0]:
    print("$20")
else:
    print("$100")