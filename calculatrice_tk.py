# -*- coding: utf-8 -*-

#-----------------------IMPORTATION------------------------#
from tkinter import *
from Pile import Pile

#-------------------------------------------------------FONCTION---------------------------------------------------#

pile_bouton = Pile()    #sert à empiler les nombres tapé avec les boutons de la culculatrice puis on convertie la pile en str et on l'affiche a l'aide de barre.set()

def conv_p_s(pile):
    """fonction qui prend une pile en paramètre et renvoie une chaine de caractère
    , elle sert à convertie une pile en chaine de caractère"""
    strconv = ""
    while pile.est_vide() != True:
        strconv = pile.sommet() + strconv
        pile.depiler()
    for i in range(len(strconv)):
        pile_bouton.empiler(strconv[i])
    return strconv

def pile_tri(pile_a_trier):
    """fonction qui permet de séparer les chiffres et de les fusionner afin d'en avoir seulement deux pour une opération"""
    if " " not in conv_p_s(pile_a_trier):
        return pile_a_trier
    pile_a_trier = conv_p_s(pile_a_trier)
    stock = ""
    tabsin = ["+","-","x","/"]
    tabsigne = []
    piletri = Pile()

    for i in pile_a_trier:
        if i.isnumeric() == True or i == ".":
            stock += i
        if i == " " or i in tabsin:
            piletri.empiler(stock)
            stock = ""
        if i in tabsin:
            tabsigne.append(i)
    for j in range(len(tabsigne)):
        piletri.empiler(tabsigne[j])
    return piletri

def syn_verif(pile_a_verif):
    tabnb = []
    tabsin = []
    signe = ["+","-","x","/"]
    for i in pile_a_verif.lst:
        if i == "":
            i = " "
        if i in signe:
            tabsin.append(i)
        if i not in tabsin and i != " ":
            tabnb.append(i)
    if len(tabnb) == len(tabsin) or len(tabnb) < len(tabsin):#si il y a autant de chiffre que de signe alors la syntaxe est incorrect ou si il y a plus de nombre que de signe il faudra vérifier si elle n'en comporte pas trop
        barre.set("Erreur Syntaxe")
        return False
    else:
        if len(tabnb) > len(tabsin) and len(tabnb)-1 == len(tabsin):#regarde si il y a le nombre exact de nombre par rapport au singe exemple: 33+, 2 nb 2-1 = 1 = le nombre de signe
            return True
        else:
            barre.set("Erreur Syntaxe")
            return False

def quitte():
    """sert à quitter la calculatrice"""
    fenetre.destroy()
    return
#-----------------------------------------------------------------------------------------------------------------#

#------------------------------------------FONCTION DE CALCUL-----------------------------------------------------#

def evalpostfixee(exp):

    """fonction qui prend en paramètre une chaine de caratère
     de la chaine de caractère"""

    pile = pile_tri(exp)#pile qui receptionne les chiffres
    assert(syn_verif(pile) == True),"erreur vous avez mal formulé le calcul"

    exp = conv_p_s(exp)
    tabsign = ['x', '-', '+', '/']
    for i in exp:
        if i in tabsign :#si le signe est dans le tableau
            nb1 = pile.lst[0]
            nb2 = pile.lst[1]
            if nb1.isnumeric() == False:
                nb1 = float(nb1)
            else:
                nb1 = int(nb1)
            if nb2.isnumeric() == False:
                nb2 = float(nb2)
            else:
                nb2 = int(nb2)
            #--------------opération-----------------#
            if i == 'x':
                calcul = nb1 * nb2
                pile.empiler(str(calcul))
            if i == '+':
                calcul = nb1 + nb2
                pile.empiler(str(calcul))
            if i == '-':
                calcul = nb2 - nb1
                pile.empiler(str(calcul))
            if i == '/':
                calcul = nb2 / nb1
                pile.empiler(str(calcul))
    return pile.sommet()
#-------------------------------------------------------------------------------------------------------------------#

#---------------------------- CREATION DE LA FENETRE -------------------------------#

fenetre = Tk()
fenetre.configure(bg = ('black'))

#-----------------------CREATION DE LA BARRE D'AFFICHAGE-------------------------#

barre = StringVar()
barre.set("0")
reglagebarre = Entry(bg = 'black', fg = 'yellow' , bd = 3,font = ('arial', 15,'bold') , textvariable = barre, selectborderwidth = 1, insertwidth = 1, justify = 'right').grid(columnspan = 5, row = 0, rowspan = 2) #reglage de la barre d'affichage des calculs

#--------------------BOUTON CHIFFRE--------------------#

bouton7 = Button(fenetre, text ='7', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton( "7")).grid(column = 0, row = 3)
bouton4 = Button(fenetre, text ='4', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton( "4")).grid(column = 0, row = 4)
bouton1 = Button(fenetre, text ='1', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton( "1")).grid(column = 0, row = 5)
space = Button(fenetre, text ='--', padx = 19, pady = 20, bg = '#F39D0F', fg = 'white', bd = 5, command = lambda:bouton(" ")).grid(column = 0, row = 6)

bouton0 = Button(fenetre, text ='0', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton( "0")).grid(column = 1, row = 6)
bouton8 = Button(fenetre, text ='8', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton( "8")).grid(column = 1, row = 3)
bouton5 = Button(fenetre, text ='5', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton( "5")).grid(column = 1, row = 4)
bouton2 = Button(fenetre, text ='2', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton( "2")).grid(column = 1, row = 5)

bouton9 = Button(fenetre, text ='9', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton( "9")).grid(column = 2, row = 3)
bouton6 = Button(fenetre, text ='6', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton( "6")).grid(column = 2, row = 4)
bouton3 = Button(fenetre, text ='3', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton( "3")).grid(column = 2, row = 5)

#-------------------BOUTON SIGNE-----------------------#

bouton_plus = Button(fenetre, text ='+', padx = 15, pady = 15, bg = '#F39D0F', fg = 'white' , bd = 5, command = lambda:bouton("+")).grid(column = 4, row = 4)
bouton_division = Button(fenetre, text ='/', padx = 15, pady = 14, bg = '#F39D0F', fg = 'white' , bd = 5, command = lambda:bouton("/")).grid(column = 4, row = 2)
bouton_moins = Button(fenetre, text ='-', padx = 15, pady = 15, bg = '#F39D0F', fg = 'white' , bd = 5, command = lambda:bouton("-")).grid(column = 4, row = 5)
bouton_multiplier = Button(fenetre, text ='x', padx = 15, pady = 15, bg = '#F39D0F', fg = 'white' , bd = 5, command = lambda:bouton( "x")).grid(column = 4, row = 3)
bouton_egale = Button(fenetre, text ='=', padx = 15, pady = 15, bg = '#F39D0F', fg = 'white' , bd = 5, command = lambda:bouton("=")).grid(column = 4, row = 6)
bouton_del = Button(fenetre, text = 'DEL', padx = 15, pady = 15, bg = '#F39D0F', fg = 'white', bd = 5, command = lambda:bouton("del")).grid(column = 5, row = 2)
bouton_virgule = Button(fenetre, text =',', padx = 15, pady = 15, bg = '#F39D0F', fg = 'white' , bd = 5, command = lambda:bouton(",")).grid(column = 2, row = 6)
bouton_AC = Button(fenetre, text ='AC', padx = 15, pady = 15, bg = '#756D61', command = lambda:bouton('AC')).grid(column = 0, row = 2)
bouton_negatif = Button(fenetre, text ='-/+', padx = 15, pady = 15, bg = '#756D61', command = lambda:bouton("negatif")).grid(column = 1, row = 2)
bouton_pourcent = Button(fenetre, text ='%', padx = 17, pady = 15, bg = '#756D61', command = lambda:bouton("pourcent")).grid(column = 2, row = 2)
bouton_quitter = Button(fenetre, text = "QUIT", padx = 15, pady = 15, bg = '#FFFFFF', command = lambda:quitte()).grid(column = 5, row = 7)
bouton_change_mode = Button(fenetre, text = 'mode', padx = 15, pady = 15, bg = '#FFFFFF', command = lambda:change_mode()).grid(column = 5, row = 1)

#--------------------------------------FONCTION POUR BOUTON DIRECT----------------------------------------#

def bouton(strnb):
    """fonction qui prend un paramètre un String et renvoie None.
    Elle sert au fonctionnalité des bouton"""
    tabsigne = ["+","-","/","x"]
#----------------------------BOUTON signe------------------------------#
    if strnb in tabsigne :
        pile_bouton.empiler(strnb)
        barre.set(conv_p_s(pile_bouton))
        return
#---------------------------------------------------------------------#
#--------------------------Pour les nombres---------------------------#
    if strnb.isnumeric() == True:
        pile_bouton.empiler(strnb)
        barre.set(conv_p_s(pile_bouton))
        return
#---------------------------------------------------------------------#
#---------------------------BOUTON ESPACE-----------------------------#
    if strnb == " ":
        pile_bouton.empiler(strnb)
        barre.set(conv_p_s(pile_bouton))
        return
#---------------------------------------------------------------------#
#------------------------------BOUTON DEL-----------------------------#
    if strnb == "del":
        if pile_bouton.hauteur() <= 1:
            pile_bouton.depiler()
            barre.set("0")
        if pile_bouton.hauteur() > 1:
            pile_bouton.depiler()
            barre.set(conv_p_s(pile_bouton))
        return
#---------------------------------------------------------------------#
#----------------------------BOUTON EGAL------------------------------#
    if strnb == "=" :
        egale(pile_bouton)
        return
#---------------------------------------------------------------------#
#-----------------------------BOUTON AC-------------------------------#
    if strnb == 'AC':
        while pile_bouton.est_vide() == False:
            pile_bouton.depiler()
        pile_bouton.empiler("")
        barre.set("0")
        return
#---------------------------------------------------------------------#
#-------------------------------BOUTON %------------------------------#
    if strnb == "pourcent":
        pile_bouton.empiler("%")
        barre.set(conv_p_s(pile_bouton))
        pile_bouton.depiler()
        pilecopie = conv_p_s(pile_bouton)
        for j in range(pile_bouton.hauteur()):
            pile_bouton.depiler()
        pile_bouton.empiler("100 ")
        for elem in pilecopie:
            pile_bouton.empiler(elem)
        pile_bouton.empiler("/")
        return
#---------------------------------------------------------------------#
#---------------------------BOUTON VIRGULE----------------------------#
    if strnb == ",":
        pile_bouton.empiler(".")
        barre.set(conv_p_s(pile_bouton))
        return
#---------------------------------------------------------------------#
    return
#---------------------------BOUTON EGALE------------------------------#
def egale(pile):
    """fonction qui prend un paramètre une pile et qui renvoie None """
    calcul = evalpostfixee(pile)
    barre.set(calcul)
    while pile_bouton.est_vide() == False:#sert à mettre le résultat du calcul dans la pile
        pile_bouton.depiler()
        pile_bouton.empiler(str(calcul))
        return
#---------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------#


fenetre.mainloop()
#ajouter la pavé numérique