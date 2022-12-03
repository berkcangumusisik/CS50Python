"""Anahtar sözcük with, bir dosyanın kapanmasını otomatikleştirmenizi sağlar.
"""

name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
