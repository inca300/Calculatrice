#EXERCICE 3

from Pile import Pile
from tkinter import messagebox as tkmsbx

def evalpostfixee(exp):
    assert(type(exp) == str),"erreur la variable str n'est pas une chaine de caractère"
    pile = Pile()
    tabsign = ['x', '-', '+', '/']
    for i in exp:
        if i in tabsign :#si le signe est dans le tableau
            assert(pile.est_vide() == False),""
            nb1 = pile.sommet()
            pile.depiler()
            nb2 = pile.sommet()
            pile.depiler()
            if i == 'x':
                calcul = nb1 * nb2
                pile.empiler(calcul)
            if i == '+':
                calcul = nb1 + nb2
                pile.empiler(calcul)
            if i == '-':
                calcul = nb2 - nb1
                pile.empiler(calcul)
            if i== '/':
                calcul = nb2 / nb1
                pile.empiler(calcul)
        else:
            pile.empiler(int(i))
    return pile.sommet()
"""
assert(evalpostfixee('12+3+') == 6 ),'erreur'
assert(evalpostfixee('12+3x') == 9 ),'erreur'
assert(evalpostfixee('123x+') == 7),'erreur'
assert(evalpostfixee('27+85-x') == 27),'erreur'
assert(evalpostfixee('82/') == 4 ),'erreur'
assert(evalpostfixee('55x5+') == 30),'erreur'
"""
def exp_parenthese(exp):
    pilepar = Pile()
    for i in exp:
        if i == '(':
            pilepar.empiler(i)
        if i == ')':
            if pilepar.est_vide() == True:
                return False, "il y a trop de parenthèse fermante"
            pilepar.depiler()
    if pilepar.est_vide() == False:
        return False, "il y a trop de parenthèse ouvrante"
    return True

#asserexp_parenthese('(((42+)2x)))))')

