# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip() # strip, kullanıcı girişinin solundaki ve sağındaki tüm boşlukları kaldırır.

# Print the output
print(f"hello, {name}")


# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Capitalize the first letter of each word
name = name.title() # title kullanıcının adını büyük/küçük harfe yazar

# Print the output
print(f"hello, {name}")

# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# Print the output
print(f"hello, {name}")