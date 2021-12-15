from Pile import Pile

def evalpostfixee(exp):

    """fonction qui prend en paramètre une chaine de caratère
    et qui renvoie le sommet d'une pile qui représente le résultat du calcul
    de la chaine de caractère"""

    assert(type(exp) == str),"erreur la variable str n'est pas une chaine de caractère"

    pile = Pile()
    tabsign = ['x', '-', '+', '/']
    for i in exp:
        if i in tabsign :#si le signe est dans le tableau
            assert(pile.est_vide() == False),"Votre opération n'est pas formulé correctement\nERREUR !"
            if pile.sommet() == "_":
                pile.depiler()
                nb1 = pile.sommet()
            else:
                nb1 = pile.sommet()
                pile.depiler()
            if pile.sommet() == "_":
                pile.depiler()
                nb2 = pile.sommet()
            else:
                nb2 = pile.sommet()
                pile.depiler()
            if i == 'x':
                calcul = int(nb1) * int(nb2)
                pile.empiler(calcul)
            if i == '+':
                calcul = int(nb1) + int(nb2)
                pile.empiler(calcul)
            if i == '-':
                calcul = int(nb2) - int(nb1)
                pile.empiler(calcul)
            if i== '/':
                calcul = int(nb2) / int(nb1)
                pile.empiler(calcul)
        else:
            reste = pile.sommet()
            if i != " ":
                pile.empiler(i)
            else:
                while reste != "vide" or reste != " " or reste != "_":
                    stock1 = pile.sommet()
                    pile.depiler()
                    stock2 = pile.sommet()
                    print("i =",i,"\n","pile =",pile,"\n","sommet =",pile.sommet(),"\n","stock :",stock1, stock2)
                    pile.depiler()
                    reste = pile.sommet()
                    pile.empiler(stock2 + stock1)
                pile.empiler("_")
                reste = pile.sommet()
    return pile.sommet()

assert(evalpostfixee("123 45 +") == "168"),"erreur"

#problème car il prend en compte le _ et fusionne 123_45 donc
#impossible de faire le calcule de plus je prend en compte le _ durant la phrase de calcule