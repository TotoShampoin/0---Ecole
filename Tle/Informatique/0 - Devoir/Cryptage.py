text = input("Entrez le message : ")
letters = input("Entrez le code : ")

text2 = ""      # Le futur message crypté
d = 0           # Code ASCII de la lettre

for i in text:
    d = ord(i)
    if letters.upper().find(i.upper())!=-1: # i et letters sont temporairement convertis pour reconnaître majuscules et minuscules
        if d>64 and d<91:                   # MAJUSCULE
            text2 += chr(((d-63)%26)+65)
        elif d>96 and d<123:                # minuscule
            text2 += chr(((d-95)%26)+97)
        elif d>47 and d<58:                 # N0mbr3
            text2 += chr(((d-46)%26)+48)
    else:
        text2 += i

print(text2)
