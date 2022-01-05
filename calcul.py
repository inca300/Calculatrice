# Créé par PUISSEE, le 13/12/2021 en Python 3.4
def calcul(pile):
    nbr1 = ""
    nbr2 = ""
    operator = ""
    operator_check = False
    for i in pile.lst:
        if i.isnumeric() and operator_check == False:
            nbr1 += i
        elif i.isnumeric() == False:
            operator = i
            operator_check = True
        else:
            nbr2 = i
    if operator == "+":
        result = int(nbr1) + int(nbr2)
    elif operator == "x":
        result =  int(nbr1) *int(nbr2)
    elif operator == "/":
        result =  int(nbr1) / int(nbr2)
    elif operator == "-":
        result =  int(nbr1) - int(nbr2)
    return str(result)




