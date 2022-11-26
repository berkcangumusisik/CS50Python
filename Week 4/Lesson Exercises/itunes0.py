"""
API'ler veya "uygulama programı arayüzleri", başkalarının koduna bağlanmanıza izin verir.
requests programınızın bir web tarayıcısı gibi davranmasını sağlayan bir pakettir.

"""

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])