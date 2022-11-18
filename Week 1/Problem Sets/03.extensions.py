"""
Dosya uzantıları
Windows ve macOS bazen bunları gizlese de, çoğu dosyanın dosya uzantıları. vardır, bu dosya adlarının sonunda nokta ( ) ile başlayan bir son ektir . Örneğin, GIF'ler için dosya adları ile biter ve JPEG'ler.gif için dosya adları veya ile biter . Bir dosyayı açmak için çift tıkladığınızda, bilgisayarınız hangi programın başlatılacağını belirlemek için dosya uzantısını kullanır..jpg.jpeg

Web tarayıcıları ise aksine, web'de yaşayan dosyaların nasıl görüntüleneceğini belirlemek için önceden MIME türleri olarak bilinen ortam türlerini kullanır. Bir web sunucusundan dosya indirdiğinizde, bu sunucu dosyanın kendisi ile birlikte dosyanın ortam türünü belirten bir HTTP başlığı gönderir. Örneğin, bir GIF image/gifiçin ortam türü ve bir JPEG için ortam türü image/jpeg. Bir dosyanın ortam türünü belirlemek için, bir web sunucusu genellikle dosyanın uzantısına bakar ve birini diğerine eşler.

Yaygın türler için Developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types adresine bakın .

adlı bir dosyada extensions.py, kullanıcıdan bir dosyanın adını soran ve dosyanın adı büyük/küçük harfe duyarsız olarak şu son eklerden herhangi birinde bitiyorsa dosyanın ortam türünü çıkaran bir program uygulayın:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
Dosyanın adı başka bir son ekle bitiyorsa veya hiç son eki yoksa, application/octet-streambunun yerine çıktı alın, bu yaygın bir varsayılandır.
"""

answer = input("File name : ")
answer = answer.lower()
if ".gif" in answer:
    print("image/gif")
elif ".jpg" in answer:
    print("image/jpeg")
elif ".jpeg" in answer:
    print("image/jpeg")
elif ".png" in answer:
    print("image/png")
elif ".pdf" in answer:
    print("application/pdf")
elif ".txt" in answer:
    print("text/plain")
elif ".zip" in answer:
    print("application/zip")
else:
    print("application/octet-stream")