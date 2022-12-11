"""
^ dizenin başlangıcıyla eşleşir
$, dizenin sonuyla veya dizenin sonundaki yeni satırın hemen öncesiyle eşleşir
"""

import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")