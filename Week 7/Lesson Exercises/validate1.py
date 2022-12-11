email = input("Enter your email address: ").strip()
if "@" in email and "." in email:
    print("Your email address is valid")
else:
    print("Your email address is invalid")