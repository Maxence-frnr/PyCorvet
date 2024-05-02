import random

pos = []
nombre_de_caracter = 32
nombre_de_points = 4096
for i in range(nombre_de_points):
    x = random.randint(0, nombre_de_caracter*5)
    y = random.randint(0, nombre_de_caracter*4)
    pos.append((x, y))

def separate_bigs_and_smalls(matrix):
    big = []
    small = []
    for i in range(len(matrix)):
        big.append((matrix[i][0]//5, matrix[i][1]//8))
        small.append((matrix[i][0]%5, matrix[i][1]%8))
    return [big, small]    
                           
def regroup_list(big, small):                         
    liste = []
    for i in range(len(big)):                                                                                   
        liste.append((big[i], small[i]))
    return liste

def regroup_by_caracter(matrix):
    global nombre_de_caracter
    list_of_caracter = []

    for i in range(nombre_de_caracter):
        list_of_caracter.append([])

    for i in range(len(list_of_caracter)//2):
        for j in range(len(matrix)):
            if matrix[j][0][1] < 1 and matrix[j][0][0] == i:
                list_of_caracter[i].append((matrix[j][1][0], matrix[j][1][1]))
            elif matrix[j][0][1] >= 1 and matrix[j][0][0] == i:
                list_of_caracter[i+nombre_de_caracter//2].append((matrix[j][1][0], matrix[j][1][1]))
    return list_of_caracter

def create_caracter(car: list):
    caracter = []
    for y in range(8):
        caracter.append([])
        for x in range(5):
            caracter[y].append(0)

    for i in range(len(car)):
        for y in range(len(caracter)):
            for x in range(len(caracter[y])):
                if car[i][0] == x and car[i][1] ==y:
                    caracter[y][x] = 1
    return caracter

def create_all_caracter(matrix):
    all_caracter = []
    for i in range(len(matrix)):
        caractere = create_caracter(matrix[i])
        all_caracter.append(caractere)

    return all_caracter
    
def print_caracter(caracter):
    for y in range(len(caracter)):
        print(caracter[y])

def add_0_in_hexa(txt:str):
    txt = list(txt)
    if len(txt) < 4:
        txt.insert(2, '0')
    txt[1] = txt[1].lower()
    txt = ''.join(txt)
    return txt

def list_to_hexadecimal(caracter):
    new_caracter = []
    for y in range(len(caracter)):
        value = 0
        for x in range(len(caracter[y])):
            if x == 0 and caracter[y][x] == 1:
                value +=1
            elif x!=0 and caracter[y][x] == 1:
                value += 2**(4-x)
        value = str(hex(value))
        value = value.upper()
        value = add_0_in_hexa(value)
        new_caracter.append(value)

    return new_caracter       

def convert(matrix):
    #print('matrice de depart', matrix)
    A = separate_bigs_and_smalls(matrix)
    #print('\nmatrice separe', x)
    B = regroup_list(A[0], A[1])
    #print('\nmatrice regroupe',x)
    C = regroup_by_caracter(B)
    #print('\nmatrice regroupe par caracter',x)
    D = create_all_caracter(C)
    # for i in range(len(x)):
    #     print(i)
    #     print_caracter(x[i])
    print(D[15])
    E = list_to_hexadecimal(D[15])
    all_hexa = []
    for i in range(nombre_de_caracter):
        all_hexa.append(list_to_hexadecimal(D[i]))
    return all_hexa

def print_all_hexa(all_hexa):
    for i in range(len(all_hexa)):
        print(f'caracter {i}', all_hexa[i])
print_all_hexa(convert(pos))