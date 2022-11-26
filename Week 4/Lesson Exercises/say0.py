""" 
Python'un bu kadar popüler olmasının nedenlerinden biri, işlevsellik ekleyen çok sayıda güçlü üçüncü taraf kitaplığının olmasıdır. Bir klasör olarak uygulanan bu üçüncü taraf kitaplıklarına “paketler” diyoruz.
PyPI, şu anda mevcut olan tüm mevcut üçüncü taraf paketlerinin bulunduğu bir havuz veya dizindir.
cowsaybir ineğin kullanıcıyla konuşmasını sağlayan iyi bilinen bir pakettir.
Python, pippaketleri sisteminize hızlı bir şekilde kurmanıza izin veren bir paket yöneticisine sahiptir.
"""

import cowsay
import sys
if(len(sys.argv) == 2):
    cowsay.cow(sys.argv[1])