names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.strip())
        
for name in sorted(names, reverse=False):
    print(f"Hello {name}")