""" 

Python'da tryve exceptbir şeyler ters gitmeden önce kullanıcı girdisini test etmenin yollarıdır. Kodunuzu aşağıdaki gibi değiştirin:
"""
try:
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
    
print(f"x is {x}")
