"""
Emoji olmadan önce, :) gibi metinlerin mutlu bir yüz olduğu ve :( gibi metinlerin üzgün bir yüz olduğu ifadeler vardı. Günümüzde programlar, ifadeleri otomatik olarak emojiye dönüştürme eğilimindedir!

Faces.py adlı bir dosyada, str'yi girdi olarak kabul eden ve aynı girişi 🙂'ye dönüştürülmüş any :) (biraz gülen yüz olarak da bilinir) ve 🙁'ya dönüştürülmüş any :( (başka bir deyişle bilinen) ile döndüren convert adlı bir işlev uygulayın. biraz kaşlarını çatmış bir yüz olarak) Diğer tüm metinler değiştirilmeden iade edilmelidir.

Ardından, aynı dosyada, kullanıcıdan giriş yapmasını isteyen, bu girdiye convert çağrıları yapan ve sonucu yazdıran main adlı bir işlev uygulayın. Girdiye bağımsız değişken olarak kendi str'nizi iletmek gibi, kullanıcıdan açıkça istemekte özgürsünüz, ancak zorunlu değilsiniz. Dosyanızın altındaki main'i çağırdığınızdan emin olun.
"""
text = input()
text = text.replace(":)","🙂")
text = text.replace(":(", "🙁")
print(text)