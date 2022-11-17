"""
Bazı insanların oldukça hızlı bir şekilde ders verme alışkanlığı vardır ve onları YouTube'un 0,75'lik oynatma hızı gibi yavaşlatmak, hatta kelimeler arasında duraklatarak yavaşlatmak güzel olurdu.

Playback.py adlı bir dosyada, Python'da kullanıcıdan girdi isteyen ve ardından aynı girdiyi çıkaran, her boşluğu ... ile değiştirerek (yani, üç nokta) bir program uygulayın.
"""
sentence = input("Sentence : ")
print(sentence.replace(" ", "..."))