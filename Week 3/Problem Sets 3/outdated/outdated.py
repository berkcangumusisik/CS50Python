
"""
Amerika Birleşik Devletleri'nde tarihler genellikle ay-gün-yıl düzenine (AA/GG/YYYY) göre biçimlendirilir, aksi takdirde orta-endian düzeni olarak da bilinir ve bu muhtemelen kötü bir tasarımdır. Bu formattaki tarihler kolayca sıralanamaz çünkü tarihin yılı ilk yerine sonda gelir. Örneğin, herhangi bir programda (örneğin bir elektronik tablo) 2/2/1800, 3/3/1900, ve kronolojik olarak sıralamayı deneyin . 1/1/2000Bu formattaki tarihler de belirsizdir. Harvard 8 Eylül 1636'da kuruldu ama 8/9/1636 9 Ağustos 1636 olarak da yorumlanabilir!

Neyse ki bilgisayarlar , hangi ülkeden olursa olsun tarihlerin yıl-ay-gün (YYYY-AA-GG) düzeninde, yılları dört basamaklı, ayları iki basamaklı olarak biçimlendirmesi gerektiğini belirten uluslararası bir standart olan ISO 8601'i kullanma eğilimindedir. ve iki basamaklı günler, gerektiği şekilde her birinin başında sıfırlarla "doldurulur".

adlı bir dosyada , kullanıcıdan ay-gün-yıl sırasına göre veya gibi biçimlendirilmiş bir tarih ( anno Dominioutdated.py ) isteyen bir program uygulayın; burada, sonraki ay aşağıdaki değerlerden herhangi biri olabilir :9/8/1636September 8, 1636list
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def ConvertVerboseDate(date: str):

    if ' ' not in date:
        return date

    tokens = date.split(' ')

    if len(tokens) != 3:
        return date

    if tokens[0].title() in months:
        if tokens[1].endswith(','):
            tokens[1] = tokens[1][:-1]
        else:
            return date

        tokens[0] = months.index(tokens[0].title()) + 1
        return f'{tokens[0]}/{tokens[1]}/{tokens[2]}'

    return date

def IsMiddleEndianDate(date: str):
    if '/' not in date:
        return False

    tokens = date.split('/')

    if len(tokens) != 3:
        return False

    if tokens[0].isdigit() and tokens[1].isdigit() and tokens[2].isdigit():
        tokens[0] = int(tokens[0])
        tokens[1] = int(tokens[1])
        tokens[2] = int(tokens[2])
    else:
        return False

    if tokens[0] < 1 or tokens[0] > 12:
        return False
    if tokens[1] < 1 or tokens[1] > 31:
        return False
    if tokens[2] < 0 or tokens[2] > 9999:
        return False

    return True

def ConvertToBigEndianDate(date: str):
    month, day, year = date.split('/')
    return f'{year.zfill(4)}-{month.zfill(2)}-{day.zfill(2)}'

while True:
    date = ConvertVerboseDate(input('Date: ').strip())

    if IsMiddleEndianDate(date) == False:
        continue

    print(ConvertToBigEndianDate(date))
    break