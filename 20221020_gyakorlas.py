

def dectobin(dec):
    bin = ""
    while dec>0:
        maradek = dec % 2 
        bin = str(maradek) + bin
        dec = int(dec / 2)
    return bin



print(dectobin(192)),





























