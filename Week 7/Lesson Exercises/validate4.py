import re

email = input("Enter an email address: ")

if re.search("@",email):
    print("Your email address is valid")
else:
    print("Your email address is invalid")
    
# re.search() ile arama yapılır. Eğer aranan değer bulunursa True, bulunamazsa False döndürür.