"""
Harvard Üniversitesi'ne ev sahipliği yapan Massachusetts'te, arabanız için rastgele harfler yerine seçtiğiniz harfler ve rakamlarla gösterişli bir plaka talep etmek mümkündür. Gereksinimler arasında olsa da, şunlardır:

"Tüm makyaj plakaları en az iki harfle başlamalıdır."
“… makyaj levhaları en fazla 6 karakter (harf veya rakam) ve en az 2 karakter içerebilir.”
“Rakamlar bir levhanın ortasında kullanılamaz; sonunda gelmeleri gerekir. Örneğin, AAA222 kabul edilebilir bir makyaj masası olacaktır; AAA22A kabul edilemez. Kullanılan ilk sayı '0' olamaz.”
"Nokta, boşluk veya noktalama işaretlerine izin verilmez."
' de, kullanıcıdan bir makyaj plakası isteyen ve ardından tüm gereksinimleri karşılayıp karşılamadığını plates.pygösteren bir program uygulayın . Kullanıcının girişindeki tüm harflerin büyük olacağını varsayalım. Programınızı aşağıdakilere göre yapılandırın, burada tüm gereksinimleri karşılıyorsa ve yoksa karşılamıyorsa geri döner . a olacağını varsayalım . Aramak için ek işlevler uygulayabilirsiniz (örneğin, gereksinim başına bir işlev).ValidInvalidis_validTruesFalsesstris_valid

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...


main()
"""

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)

    if length >= 2 and length <= 6:
        for letters in s:
            if not s.isalnum():
                break

            if s[0:2].isalpha():
                middle = s[1:-1]
                if middle.isnumeric() and middle.find(0):
                    break


                zeroIndex = s.find("0") - 1

                if s[-(zeroIndex)].isdigit():
                    for x in s:
                        if x.isdigit():
                            if x.startswith('0'):
                                return False
                            else:
                                return True

                if s[-2].isdigit() and s[-1].isalpha():
                    break
                elif s[-2].isdigit():
                    return True
                elif s.isalpha():
                    return True

    else:
        return False

main()