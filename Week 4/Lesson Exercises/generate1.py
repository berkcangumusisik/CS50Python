import random
number = random.randint(1, 100)
print(number)

"""
random.randint() fonksiyonu,rastgele bir tamsayı üretir.
"""
print("-------------------")

cards = ["Jack", "Queen", "King"]
random.shuffle(cards) # shuffle() fonksiyonu, listedeki öğeleri karıştırır.
for card in cards:
    print(card)