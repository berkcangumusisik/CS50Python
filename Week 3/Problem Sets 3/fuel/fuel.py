"""
Yakıt göstergeleri, genellikle kesirlerle, bir depoda ne kadar yakıt olduğunu gösterir. Örneğin 1/4 bir deponun %25 dolu olduğunu, 1/2 bir deponun %50 dolu olduğunu ve 3/4 bir deponun %75 dolu olduğunu gösterir.

adlı bir dosyada fuel.py, kullanıcıdan, olarak biçimlendirilmiş bir kesri isteyen ve her birinin bir tam sayı olduğu ve ardından en yakın tam sayıya yuvarlanmış bir yüzde olarak depoda ne kadar yakıt olduğunu gösteren bir program X/Yuygulayın . Yine de %1 veya daha azı kalırsa, bunun yerine deponun esasen boş olduğunu belirtmek için çıktı alın. Ve %99 veya daha fazlası kalırsa, bunun yerine deponun esasen dolu olduğunu gösteren çıkış.XYEF

Yine de Xveya Ybir tamsayı değilse X, değerinden büyükse Yveya Yise 0, bunun yerine kullanıcıya tekrar sorun. Y( olması gerekli değildir .) veya 4gibi istisnaları yakaladığınızdan emin olun .ValueErrorZeroDivisionError
"""
while True:
    try:
        user = input("Fraaaction: ")
        one,two = user.split("/")
        one = int(one)
        two = int(two)
        if one > two:
            continue
    except ValueError:
        pass
    else:
        try:
            result = (one / two)
            result *= 100
            result = round(result)
            result = int(result)
        except ZeroDivisionError:
            pass
        else:
            if (result <= 1):
                print("E")
                exit()
            elif (result >= 99):
                print("F")
                exit()
            else:
                print(f"{result}%")
                exit()
