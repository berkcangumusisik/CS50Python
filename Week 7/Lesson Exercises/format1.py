import re 
name = input("What's your name? ").strip()
re.search(r"^.+, .+$", name)