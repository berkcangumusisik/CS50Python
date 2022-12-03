name = input("What's your name ?")
print("Hello", name)


names =[]
for i in range(3):
    names.append(input("What's your name ?"))


for name in sorted(names):
    print("Hello", name)