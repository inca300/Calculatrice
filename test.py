def syn_verif(pilestr):#ne prend pas encore en compte les '333+'
    tabnb = []
    tabsin = []
    for i in pilestr:
        if i == '+' or i == '-' or i == 'x' or i == '/':
            tabsin.append(i)
        else:
            tabnb.append(i)

    if len(tabnb) == len(tabsin) or len(tabnb) < len(tabsin):
        return False
    else:
        if len(tabnb) > len(tabsin) and len(tabnb)-1 == len(tabsin):
            return True
        else:
            return False