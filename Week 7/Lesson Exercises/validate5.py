"""
. yeni bir satır dışında herhangi bir karakter
* 0 veya daha fazla tekrar
+ 1 veya daha fazla tekrar
? 0 veya 1 tekrar
{m} m tekrar
{m,n} m-n tekrar
"""

import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")