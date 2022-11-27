import inflect

inflects = inflect.engine()
nameList = []
while True:
    try:
        name = input("Name: ")
        nameList.append(name)
    except EOFError:
        print()
        break

output = inflects.join(nameList)
print("Adieu, adieu, to "+ output)
