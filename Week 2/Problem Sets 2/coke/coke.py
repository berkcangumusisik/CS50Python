"""
Bir makinenin Coca-Cola (Kola) şişelerini 50 sente sattığını ve yalnızca şu kupürlerdeki madeni paraları kabul ettiğini varsayalım: 25 sent, 10 sent ve 5 sent.

adlı bir dosyada coke.py, kullanıcıdan her seferinde bir madeni para koymasını isteyen ve her seferinde kullanıcıyı ödenmesi gereken tutar hakkında bilgilendiren bir program uygulayın. Kullanıcı en az 50 sent girdikten sonra, kullanıcının borcu olan bozuk para birimi miktarını belirtin. Kullanıcının yalnızca tamsayılar gireceğini ve kabul edilen bir değer birimi olmayan herhangi bir tamsayıyı yok sayacağını varsayalım.

"""
amountDue = 50
while amountDue > 0:
    print("Amount Due " , amountDue)
    coin = int(input("Insert Coin : "))
    if coin in [25,10,5]:
        amountDue -= coin
changeOwed = abs(amountDue)
print("Change Owed : " , changeOwed)