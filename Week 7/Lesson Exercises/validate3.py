email = input("Enter your email address: ").strip()
username, domain = email.split("@")
if username and domain.endswith("edu"):
    print("Your email address is valid")
else:
    print("Your email address is invalid")