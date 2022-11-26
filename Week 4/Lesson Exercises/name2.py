import sys 
if len(sys.argv) < 2:
    sys.exit("Too few arguments") # Programdan çıkış yapar.
for arg in sys.argv[1:]:
    print("hello, my name is", arg)