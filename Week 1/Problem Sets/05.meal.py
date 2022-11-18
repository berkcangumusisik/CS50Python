""" 
Kahvaltının 7:00 ile 8:00, öğle yemeğinin 12:00 ile 13:00 ve akşam yemeğinin 18:00 ile 19:00 arasında yenmesinin adet olduğu bir ülkede olduğunuzu varsayalım. Neyi ne zaman yemeniz gerektiğini söyleyen bir programınız olsa güzel olmaz mıydı?

' meal.pyda, kullanıcıdan bir süre isteyen ve bunun breakfast time, lunch time, veya dinner time. Yemek zamanı değilse, hiçbir şey çıkarmayın. Kullanıcı girişinin 24 saat içinde #:##veya olarak biçimlendirileceğini varsayalım ##:##. Ve her öğünün zaman aralığının kapsayıcı olduğunu varsayalım. Örneğin, saat 7:00, 7:01, 7:59 veya 8:00 veya bunların arasında herhangi bir zamanda kahvaltı zamanıdır.

Programınızı aşağıdakine göre yapılandırın, burada 24 saat biçimindeki a'yı a olarak karşılık gelen saat sayısına dönüştüren ( convertile çağrılabilen) bir işlevdir . Örneğin verilen bir beğeni (yani 7 saat 30 dakika) geri dönmelidir (yani 7.5 saat).maintimestrfloattime"7:30"convert7.5

def main():
    ...


def convert(time):
    ...


if __name__ == "__main__":
    main()
"""

def main():
    exp = input('What time is it? ').strip()
    t = convert(exp)
    if 7 <= t <= 8:
        print('breakfast time')
    elif 12 <= t <= 13:
        print('lunch time')
    elif 18 <= t <= 19:
        print('dinner time')
    else:
        pass



def convert(time):
    if time.find(' ') != -1:
        t, p = time.split()
        h, m = t.split(':')
    else:
        h, m = time.split(':')
        p = 'not set'
    try:
        h = int(h)
        m = int(m)
    except ValueError:
        quit('Invalid format')
    else:
        if p == 'p.m.':
            return 12 + h + m / 60
        return h + m / 60



if __name__ == "__main__":
    main()