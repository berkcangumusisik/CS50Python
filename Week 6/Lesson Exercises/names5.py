with open("names.txt", "r") as file:
    for line in file:
        print(f"Hello {line.strip()}")
