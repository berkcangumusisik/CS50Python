"""
Bahşiş Hesaplayıcı
Ve şimdi Sihirbaz bahşiş hesaplayıcım için.

—Morty Seinfeld

Amerika Birleşik Devletleri'nde, bir restoranda yemek yedikten sonra sunucunuza, genellikle yemek maliyetinizin %15'i veya daha fazlasına eşit bir miktarda bahşiş bırakmak adettendir. Endişelenmeyin, aşağıda sizin için bir bahşiş hesaplayıcı yazdık!

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main()
Bahşiş hesaplayıcının çoğunu sizin için yazdık . Ne yazık ki, iki işlevi uygulamak için zamanımız olmadı:

dollars_to_float, giriş olarak a kabul etmelidir str( , olarak biçimlendirilmiştir $##.##, burada her #biri bir ondalık basamaktır), baştaki 'yi kaldırın $ve miktarı bir olarak döndürün float. Örneğin, $50.00girdi olarak verildiğinde, döndürmesi gerekir 50.0.
percent_to_floata'yı giriş olarak kabul etmesi gereken str(, olarak biçimlendirilmiş ##%, burada her #biri bir ondalık basamaktır), sondaki 'yi kaldırın %ve yüzdeyi a olarak döndürün float. Örneğin, 15%girdi olarak verildiğinde, döndürmesi gerekir 0.15.
Kullanıcının değerleri beklenen biçimlerde gireceğini varsayalım.
"""

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar = d.replace("$","")
    return float(dollar)


def percent_to_float(p):
    percent = p.replace("%","")
    return float(percent) / 100



main()