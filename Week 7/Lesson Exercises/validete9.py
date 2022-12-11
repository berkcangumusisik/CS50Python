"""
\d ondalık basamak
\D ondalık basamak değil boşluk karakterleri
\IS bir boşluk karakteri değil
\kelime karakteri, sayılar ve alt çizgi ile
\W kelime karakteri değil
"""


import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")