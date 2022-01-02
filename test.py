from Pile import Pile

def pile_tri(pile_a_trier):
    """fonction qui permet de séparer les chiffres et de les fusionner afin d'en avoir seulement deux pour une opération"""
    #ple_a_trier = conv_p_s(pile_a_trier)
    stock = ""
    tabsin = ["+","-","x","/"]
    tabsigne = []
    piletri = Pile()
    for i in pile_a_trier:
        if i.isnumeric() == True:
            stock += i
        if i == " " or i in tabsin:
            piletri.empiler(stock)
            stock = ""
        if i in tabsin:
            tabsigne.append(i)
    for j in range(len(tabsigne)):
        piletri.empiler(tabsigne[j])
    return piletri

def syn_verif(chaine):#dit pouvoir verifier qu'il n'y a que des chiffre ou des espaces(pas deux cote a cote)
    tabnb = []
    tabsin = []
    signe = ["+","-","x","/"]

    for i in chaine.lst:
        if i in signe:
            tabsin.append(i)
        if i not in tabsin and i != " ":
            tabnb.append(i)
    print(tabnb, tabsin)
    if len(tabnb) == len(tabsin) or len(tabnb) < len(tabsin):#si il y a autant de chiffre que de signe alors la syntaxe est incorrect ou si il y a plus de nombre que de signe il faudra vérifier si elle n'en comporte pas trop
        #barre.set("Erreur Syntaxe")
        return False
    else:
        if len(tabnb) > len(tabsin) and len(tabnb)-1 == len(tabsin):#regarde si il y a le nombre exact de nombre par rapport au singe exemple: 33+, 2 nb 2-1 = 1 = le nombre de signe
            return True
        else:
            #barre.set("Erreur Syntaxe")
            return False

test = Pile()
test.empiler("1")
test.empiler("2")
test.empiler("8")
test.empiler(" ")
test.empiler("7")
test.empiler("2")
test.empiler("+")

syn_verif(pile_tri("128 72+"))