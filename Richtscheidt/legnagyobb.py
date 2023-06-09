list = [3.29,2.92,3.50,3.07,4.27,3.14,2.88,4.00,4.88,2.88,3.43]

def legnagyobb(list):
    max = list[0]
    for szam in list:
        if szam > max:
            max = szam
    return max

def legkisebb(list):
    min = list[0]
    for szam in list:
        if szam < min:
            min = szam
    return min

def atlag(list):
    oszeg = 0
    for szam in list:
        oszeg = szam + oszeg
    return oszeg/ len(list)
def maganhangzo(szoveg):
    maganhangzok = ["a","á","e","é","u","ú","i","í","o","ó","ö","ő","ü","ű"]
    db=0
    for karakter in szoveg:
        if karakter.lower() in maganhangzok:
            db +=1
    return db

szoveg = "Árvíztűrő ütvefúrógép"
darab= maganhangzo(szoveg)
print(f"a szövegben {darab} darab magánhangzó van.")

szam2= legkisebb(list)
szam= legnagyobb(list)
atlag= atlag(list)
print(f"a lista legnagyobb eleme:{szam}")
print(f"a lista átlaga:{atlag}")
print(f"a lista legkisebb eleme:{szam2}")


