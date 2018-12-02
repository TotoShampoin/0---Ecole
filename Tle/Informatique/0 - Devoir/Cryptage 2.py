alpha  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha2 = "CDEFGHIJKLMNOPQRSTUVWXYZAB"

message  = input("Entrez votre message : ").upper()
message2 = ""

key  = input("Entrez la clé : ").upper()
key2 = ""

for i in key:
    key2 += alpha2[alpha.find(i)]

for i in message:
    if key.find(i)!= -1 :
        message2 += key2[key.find(i)]
    elif "ÀÁÂÃÄ".find(i)!= -1:
        message2 += "C"
    elif "ÈÉÊË".find(i)!= -1:
        message2 += "G"
    elif "ÌÍÎÏ".find(i)!= -1:
        message2 += "K"
    elif "ÒÓÔÕÖ".find(i)!= -1:
        message2 += "Q"
    elif "ÙÚÛÜ".find(i)!= -1:
        message2 += "W"
    elif "Ý".find(i)!= -1:
        message2 += "A"
    elif "Æ".find(i)!= -1:
        message2 += "CG"
    elif "Œ".find(i)!= -1:
        message2 += "QG"
    else:
        message2 += i

print(message2)
