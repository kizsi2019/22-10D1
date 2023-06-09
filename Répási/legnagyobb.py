def legnagyobb(list):
    max=list[0]
    for valami in list:
        if valami > max:
            max = valami
    return max

def legkisebb(list):
    min=list[0]
    for kicsi in list:
        if kicsi < min:
            min = kicsi
    return


def atlag(list):
    össz=0
    for elem in list:
        össz = elem + össz
    return össz/ len (list)

def maganhangzol(managhangzok):
    maganhangzok = ["a","á","ö","ő","u","ú","o","ó","e","é","ü","ű",]

    db = 0
    for karakter in maganhangzok:
        if karakter.lower() in maganhangzok:
            db +=1
    return db

szöveg = 'Árvíztűrő tükörfúrógép'
darab = maganhangzol(szöveg)
print("A szövegben ennyi magánhangzó van:", darab)

list = [3.29,2.23,3.14,2.22,3.00,4.00,2.00,4.00,5.00,2.14,3.29]
szam = legnagyobb(list)
atlag=atlag(list)
print(f'A lista legnagyobb eleme:{szam}')
print(f'A lista átlaga:{atlag}')
