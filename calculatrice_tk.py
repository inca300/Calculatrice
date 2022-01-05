# -*- coding: utf-8 -*-

#-----------------------IMPORTATION------------------------#
from tkinter import *
from tkinter import ttk
from Pile import Pile
from calcul import calcul
#-------------------------------------------------------FONCTION---------------------------------------------------#

pile_bouton = Pile()    #sert à empiler les nombres tapé avec les boutons de la culculatrice puis on convertie la pile en str et on l'affiche a l'aide de barre.set()
mode = ""
def conv_p_s(pile):
    """fonction qui prend en paramètre une pile et renvoie une chaine de caractère
    elle sert à convertie une pile en chaine de caractère"""
    strconv = ""
    for i in pile.lst:
        strconv = strconv + i
    return strconv

def pile_tri(pile_a_trier):
    """fonction qui prend en paramètre une pile pile_a_trier et renvoie une pile.
    Cette fonction permet de fusionner les chiffres écrit séparément dans une pile
    afin d'en avoir le nombre de chiffres nécéssaires pour effectuer une opération"""
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
    """Fonction qui prend en paramètre une pile pile_a_verif et renvoie un booléen.
    Cette fonction permet de vérifier la syntaxe d'une opération avant de l'effectuer
    afin d'effectuer l'oppération ou non"""
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
    if mode == 'polo':
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

    """fonction qui prend en paramètre une pile exp et renvoie une chaine de caractère.
    Cette fonction permet de faire un calcul avec la notation polonaise inversé"""

    pile = pile_tri(exp)#pile qui receptionne les chiffres
    assert(syn_verif(pile) == True),"erreur vous avez mal formulé le calcul"

    exp = conv_p_s(exp)
    tabsign = ['x', '-', '+', '/']
    for i in exp:
        if i in tabsign :#si le signe est dans le tableau
            #------------initialisation des nombres a calculé---------#
            nb1 = pile.lst[0]
            nb2 = pile.lst[1]
            if nb1.isnumeric() == False:#pour convertir un string en float
                nb1 = float(nb1)
            else:                       #pour convertir un string en int
                nb1 = int(nb1)
            if nb2.isnumeric() == False:#pour convertir un string en float
                nb2 = float(nb2)
            else:                       #pour convertir un string en int
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

#--------------------------------------FONCTION POUR BOUTON DIRECT----------------------------------------#

def bouton(strnb):
    """fonction qui prend un paramètre un String et renvoie None.
    Elle sert au fonctionnalité des bouton
    plus précisément au fonction lié a son bouton car chaque bouton
    envoie une chaine de caractère précis qui lors de la fonction est
    traité afin de répondre a l'une des condition dans la fonction"""

    tabsigne = ["+","-","/","x"]
#----------------------------BOUTON signe------------------------------#
    if strnb in tabsigne :#empiler le signe du bouton préssé et affiche la pile convertie sous forme de caractèreo
        pile_bouton.empiler(strnb)
        barre.set(conv_p_s(pile_bouton))
        return
#---------------------------------------------------------------------#
#--------------------------Pour les nombres---------------------------#
    if strnb.isnumeric() == True:#empile si strnb est un nombre
        pile_bouton.empiler(strnb)
        barre.set(conv_p_s(pile_bouton))
        return
#---------------------------------------------------------------------#
#---------------------------BOUTON ESPACE-----------------------------#
    if strnb == " ":#empiler si strnb est un espace
        pile_bouton.empiler(strnb)
        barre.set(conv_p_s(pile_bouton))
        return
#---------------------------------------------------------------------#
#------------------------------BOUTON DEL-----------------------------#
    if strnb == "del":#depile le dernier nombre ajouté à la pile
        if pile_bouton.est_vide() == True:
            return
        if pile_bouton.hauteur() <= 1:
            pile_bouton.depiler()
            barre.set("0")
        if pile_bouton.hauteur() > 1:
            pile_bouton.depiler()
            barre.set(conv_p_s(pile_bouton))
        return
#---------------------------------------------------------------------#
#----------------------------BOUTON EGAL------------------------------#
    if strnb == "=" :#lance la fonction égal
        egale(pile_bouton)
        return
#---------------------------------------------------------------------#
#-----------------------------BOUTON AC-------------------------------#
    if strnb == 'AC':#depiler toute la pile et affiche 0 sur la barre
        while pile_bouton.est_vide() == False:
            pile_bouton.depiler()
        pile_bouton.empiler("")
        barre.set("0")
        return
#---------------------------------------------------------------------#
#-------------------------------BOUTON %------------------------------#
    if strnb == "pourcent":# depiler la pile afin d'ajouter "100 "pour diviser ce qui à été depiler préalablement stocker dans une autre pile
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
    if strnb == ",":#empile un "." quand strnb est une virgule
        pile_bouton.empiler(".")
        barre.set(conv_p_s(pile_bouton))
        return
#---------------------------------------------------------------------#
#---------------------------BOUTON NEGATIF----------------------------#
    if strnb == "negatif":
        pilenegatif = pile_tri(pile_bouton)
        if pilenegatif.hauteur() == 1:
            pile_bouton.empiler("-1")
            pile_bouton.empiler("x")
            barre.set(conv_p_s(pile_bouton))
            return
        else:
            return
#---------------------------------------------------------------------#
    return
#---------------------------BOUTON EGALE------------------------------#
def egale(pile):
    """fonction qui prend un paramètre une pile et qui renvoie None.
    Cette fonction permet de lancer le calcul avec la pile_bouton et
    permet l'affichage sur la barre d'affichage"""
    calculstock = ""
    if syn_verif(pile) == True and mode == "polo":#verification du mode
        calculstock = evalpostfixee(pile)
        barre.set(calculstock)
    elif mode == "normal":
        calculstock = calcul(pile)
        calcul(pile)
        barre.set(calculstock)


    for i in range(pile_bouton.hauteur()):
        pile_bouton.depiler()
    if calculstock == "0":
        barre.set("0")
        return
    for i in calculstock:
        pile_bouton.empiler(i)
    return

#---------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------#

#-------------------------------Choix du mode de la calculatrice------------------------------------#
def choix_mode(event):
    global mode
    if bouton_change_mode.get() == 'polo':
        mode = 'polo'
    elif bouton_change_mode.get() == 'normal':
        mode = 'normal'
    print("mode : " + mode)

actual_mode = StringVar()
bouton_change_mode = ttk.Combobox(fenetre, textvariable = actual_mode)
bouton_change_mode.grid(column = 5, row = 1)
bouton_change_mode['values'] = ('Choisir le mode', 'polo', 'normal')
bouton_change_mode.current(0)
bouton_change_mode.bind('<<ComboboxSelected>>', choix_mode)
#---------------------------------------------------------------------------------------------------#

fenetre.mainloop()

#erreur avec l'implémentationn du mode syntaxe vérif