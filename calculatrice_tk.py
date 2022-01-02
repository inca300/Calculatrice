# -*- coding: utf-8 -*-

#-----------------------IMPORTATION------------------------#
from tkinter import *
from tkinter import ttk
from Pile import Pile
from calcul import calcul

#region global variables

#endregion

#region calcul function
def evalpostfixee(exp):
    """fonction qui prend en paramètre une chaine de caratère
    et qui renvoie le sommet d'une pile qui représente le résultat du calcul
    de la chaine de caractère"""
    assert(type(exp) == str),"erreur la variable str n'est pas une chaine de caractère"
    pile = Pile()
    tabsign = ['x', '-', '+', '/']
    for i in exp:
        if i in tabsign :#si le signe est dans le tableau
            assert(pile.est_vide() == False),messagebox.showerror ( title = "Erreur" , message = "Votre opération n'est pas formulé correctement\nERREUR !" )
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
#endregion

#region windows init
fenetre = Tk()
#fenetre.geometry("300x400")
fenetre.configure(bg = ('black'))
#endregion

#region affichage
affi = ""               #variable qui sert à l'affichage dans la barre d'affichage
barre = StringVar()
barre.set("0")
reglagebarre = Entry(bg = 'black', fg = 'yellow' , bd = 3,font = ('arial', 15,'bold') , textvariable = barre, selectborderwidth = 1, insertwidth = 1, justify = 'right').grid(columnspan = 5, row = 0, rowspan = 2) #reglage de la barre d'affichage des calculs
#endregion

#region buttons numbers
bouton7 = Button(fenetre, text ='7', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton1( "7")).grid(column = 0, row = 3)
bouton4 = Button(fenetre, text ='4', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton1( "4")).grid(column = 0, row = 4)
bouton1 = Button(fenetre, text ='1', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton1( "1")).grid(column = 0, row = 5)
bouton0 = Button(fenetre, text ='0', padx = 51, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton1( "0")).grid(column = 0, row = 6, columnspan = 2)

bouton8 = Button(fenetre, text ='8', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton1( "8")).grid(column = 1, row = 3)
bouton5 = Button(fenetre, text ='5', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton1( "5")).grid(column = 1, row = 4)
bouton2 = Button(fenetre, text ='2', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton1( "2")).grid(column = 1, row = 5)

bouton9 = Button(fenetre, text ='9', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton1( "9")).grid(column = 2, row = 3)
bouton6 = Button(fenetre, text ='6', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton1( "6")).grid(column = 2, row = 4)
bouton3 = Button(fenetre, text ='3', padx = 20, pady = 20, bg = '#312C2C', fg = 'white' , bd = 5, command = lambda:bouton1( "3")).grid(column = 2, row = 5)
#endregion

#region buttons symbols
"""padx et pady ce sont les dimension des bouton, text c'est le texte qu'il affiche, bg c'est beackground, fg c'est forground, bd c'est bordure, command c'est pour
lancer une command en appuyant sur le bouton et le lambda sert a ne pas lancer la fonction des le lancement du programme,
 le .grid sert à situer le bouton sur des colones et des ligne(row) pour préciser columnspan et rowpsan sert a fusionner les cases"""

bouton_plus = Button(fenetre, text ='+', padx = 15, pady = 15, bg = '#F39D0F', fg = 'white' , bd = 5, command = lambda:bouton1( "+")).grid(column = 4, row = 4)
bouton_division = Button(fenetre, text ='/', padx = 15, pady = 14, bg = '#F39D0F', fg = 'white' , bd = 5, command = lambda:bouton1( "/")).grid(column = 4, row = 2)
bouton_moins = Button(fenetre, text ='-', padx = 15, pady = 15, bg = '#F39D0F', fg = 'white' , bd = 5, command = lambda:bouton1( "-")).grid(column = 4, row = 5)
bouton_multiplier = Button(fenetre, text ='x', padx = 15, pady = 15, bg = '#F39D0F', fg = 'white' , bd = 5, command = lambda:bouton1( "x")).grid(column = 4, row = 3)
bouton_egale = Button(fenetre, text ='=', padx = 15, pady = 15, bg = '#F39D0F', fg = 'white' , bd = 5, command = lambda:bouton1("=")).grid(column = 4, row = 6)
bouton_del = Button(fenetre, text = 'DEL', padx = 15, pady = 15, bg = '#F39D0F', fg = 'white', bd = 5, command = lambda:bouton1("del")).grid(column = 5, row = 2)

bouton_virgule = Button(fenetre, text =',', padx = 15, pady = 15, bg = '#F39D0F', fg = 'white' , bd = 5).grid(column = 2, row = 6)

bouton_AC = Button(fenetre, text ='AC', padx = 15, pady = 15, bg = '#756D61', command = lambda:bouton1('AC')).grid(column = 0, row = 2)
bouton_negatif = Button(fenetre, text ='-/+', padx = 15, pady = 15, bg = '#756D61', command = lambda:bouton1("negatif")).grid(column = 1, row = 2)
bouton_pourcent = Button(fenetre, text ='%', padx = 15, pady = 15, bg = '#756D61', command = lambda:pourcentage()).grid(column = 2, row = 2)

bouton_quitter = Button(fenetre, text = "QUIT", padx = 15, pady = 15, bg = '#FFFFFF', command = lambda:quitte()).grid(column = 5, row = 7)


"""
#padx , pady , bd , fg , font = ('police', taille, bold / not bold) , text , bg = couleur fond de case avec # , activeforeground couleur du_ texte quand je click, activebackground c'est couleur de la case quand je click, command = lambda: unefonction
"""
#endregion

#region functions
def syn_verif(pilestr):
    """fonction permettant de vérifier la syntaxe du calcul donné ensuite à la fonction evalpostfixee"""
    tabnb = []
    tabsin = []
    for i in pilestr:
        if i == '+' or i == '-' or i == 'x' or i == '/':
            tabsin.append(i)
        else:
            tabnb.append(i)

    if len(tabnb) == len(tabsin) or len(tabnb) < len(tabsin):#si il y a autant de chiffre que de signe alors la syntaxe est incorrect ou si il y a plus de nombre que de signe il faudra vérifier si elle n'en comporte pas trop
        return False
    else:
        if len(tabnb) > len(tabsin) and len(tabnb)-1 == len(tabsin):#regarde si il y a le nombre exact de nombre par rapport au singe exemple: 33+, 2 nb 2-1 = 1 = le nombre de signe
            return True
        else:
            return False

def conv_p_s(pile):
    """fonction qui prend une pile en paramètre et renvoie une chaine de caractère
    , elle sert à convertie une pile en chaine de caractère"""
    str = ""
    while pile.est_vide() != True:
        str = pile.sommet() + str
        pile.depiler()
    return str

def quitte():
    """sert à quitter la calculatrice"""
    fenetre.destroy()
    print(pile_bouton.lst)
    return


#endregion
#region functions buttons
pile_bouton = Pile()    #sert à empiler les nombres tapé avec les boutons de la culculatrice

def bouton1(strnb):
    """fonction qui prend un paramètre un String et renvoie None.
    Elle sert au fonctionnalité des bouton"""
    global affi
    if strnb == "del" and len(affi) != 0:#pour le bouton del
        if affi == "":
            barre.set("0")
        if pile_bouton.est_vide() == False:
            sommet = str(pile_bouton.sommet())
            print(sommet, type(sommet))
            affi = affi.replace(sommet,"")#ne pas utiliser replace
            pile_bouton.depiler()
            barre.set(affi)
        return

    if strnb == "=" :#pour le bouton égale
        egale(pile_bouton, affi)
        return

    if strnb == 'AC':#pour le bouton AC
        affi = ""
        barre.set("0")
        return

    affi = affi + strnb
    barre.set(affi)
    pile_bouton.empiler(strnb)
    return

def egale(pile, affi):
    """fonction qui prend un paramètre une pile et qui renvoie None """
    pilestr = conv_p_s(pile)
    if syn_verif(pilestr) == True and mode == "polo":
        barre.set(evalpostfixee(pilestr))
        print(pile)
        return
    elif syn_verif(pilestr) and mode == "normal":
        print(calcul(pile))
        return
    else:
        barre.set("Erreur Syntaxe")
        return


def choix_mode(event):
    global mode
    if bouton_change_mode.get() == 'polo':
        mode = 'polo'
    elif bouton_change_mode.get() == 'normal':
        mode = 'normal'

def switch_mode():
    pass

#Choix du mode de la calculatrice
actual_mode = StringVar()
bouton_change_mode = ttk.Combobox(fenetre, textvariable = actual_mode)
bouton_change_mode.grid(column = 5, row = 1)
bouton_change_mode['values'] = ('Choisir le mode', 'polo', 'normal')
bouton_change_mode.current(0)
bouton_change_mode.bind('<<ComboboxSelected>>', choix_mode)



#endregion
fenetre.mainloop()

#quand j'appuie 2 fois sur Ã©gale faut afficher bien pas None
#ajouter le del
#faire %, ','
#faire les calcul avec les str avec des espace pour les chiffres plus grand
#faire une fonction convertir
#FAIRE UN PACMAN C<