from random import randint
random_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

paswdlist=[]

paslen=randint(10,22)
def randomList():
    randnum = randint(0, 61 )
    randLet = random_list[randnum]
    return randLet

while len(paswdlist) < paslen:
    randLet=randomList()
    paswdlist.append(randLet)

passwd=''.join(paswdlist)
print(f"oluşturulan şifre:{passwd}")
