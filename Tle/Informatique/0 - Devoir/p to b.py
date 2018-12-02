def p_to_b(string):
    rtn = ""            # La variable où les p sont des b
    for i in string:
        if i == 'p':
            rtn+='b'
        elif i == 'P':
            rtn+='B'
        else:
            rtn+=i
    return rtn

print("petit test avec des p p p p P P P P P !!! \n")
print(p_to_b("petit test avec des p p p p P P P P P !!!"))
