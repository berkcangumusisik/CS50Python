"""
open bir dosyayı açmanıza ve programınızda kullanmanıza izin veren, Python'da yerleşik bir işlevselliktir. İşlev open, okuyabileceğiniz veya yazabileceğiniz bir dosyayı açmanıza izin verir.

"""

name = input("What's your name ?")
file = open("names.txt", "w")
file.write(name)
file.close()