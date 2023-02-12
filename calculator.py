from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog
import tkinter as tk
import tkinter.font
import decimal
from math import pi

# Création de la fenêtre

##########################################
#color :
couleur_personnage = "red"
couleur_fond = "gray" #On peut mettre les couleurs en hexadécimal, par exemple, ici, mettre "gray" ou "#5FB691" pour du vert clair
couleur_structure = "black"
couleur_titre = "black"
couleurs_titre_categories = "red"
couleurs_message_erreurs1 = "yellow"
couleurs_lettre_erreur = "Blue"
couleurs_lettre_juste = "Green"


police_chiffre = "Rubik 20 bold"
fond_touche_chiffre = "white"
fond_touche_opérateur = "orange"
couleur_chiffre = "black"

#dimension
hauteur_page = 1000
largeur_page = 750

##########################################

fenetre = Tk()
canvas = Canvas(fenetre, width=hauteur_page, height=largeur_page, bg = couleur_fond, highlightthickness=0)
canvas.pack(padx=0, pady=0)
fenetre.geometry('400x625')
fenetre.config(bg=couleur_fond)
fenetre.title("Calculatrice")

##########################################

resultat = ""
FONT = tkinter.font.Font(size = 25)
Visuel = tkinter.Label(text = resultat, font = FONT)
Visuel.config(state = tkinter.NORMAL)


bouton1 = Button(fenetre, font=police_chiffre, bg=fond_touche_chiffre,
                 fg=couleur_chiffre, text='1', height=0, width=0,
                 command=lambda: ajout1(), padx=15, pady=5)

bouton2 = Button(fenetre, font=police_chiffre, bg=fond_touche_chiffre,
                 fg=couleur_chiffre, text='2', height=0, width=0,
                 command=lambda: ajout2(), padx=15, pady=5)

bouton3 = Button(fenetre, font=police_chiffre, bg=fond_touche_chiffre,
                 fg=couleur_chiffre, text='3', height=0, width=0,
                 command=lambda: ajout3(), padx=15, pady=5)

##########

bouton4 = Button(fenetre, font=police_chiffre, bg=fond_touche_chiffre,
                 fg=couleur_chiffre, text='4', height=0, width=0,
                 command=lambda: ajout4(), padx=15, pady=5)

bouton5 = Button(fenetre, font=police_chiffre, bg=fond_touche_chiffre,
                 fg=couleur_chiffre, text='5', height=0, width=0,
                 command=lambda: ajout5(), padx=15, pady=5)

bouton6 = Button(fenetre, font=police_chiffre, bg=fond_touche_chiffre,
                 fg=couleur_chiffre, text='6', height=0, width=0,
                 command=lambda: ajout6(), padx=15, pady=5)

##########

bouton7 = Button(fenetre, font=police_chiffre, bg=fond_touche_chiffre,
                 fg=couleur_chiffre, text='7', height=0, width=0,
                 command=lambda: ajout7(), padx=15, pady=5)

bouton8 = Button(fenetre, font=police_chiffre, bg=fond_touche_chiffre,
                 fg=couleur_chiffre, text='8', height=0, width=0,
                 command=lambda: ajout8(), padx=15, pady=5)

bouton9 = Button(fenetre, font=police_chiffre, bg=fond_touche_chiffre,
                 fg=couleur_chiffre, text='9', height=0, width=0,
                 command=lambda: ajout9(), padx=15, pady=5)

bouton0 = Button(fenetre, font=police_chiffre, bg=fond_touche_chiffre,
                 fg=couleur_chiffre, text='0', height=0, width=0,
                 command=lambda: ajout0(), padx=15, pady=5)

boutonpi = Button(fenetre, font=police_chiffre, bg=fond_touche_opérateur,
                 fg=couleur_chiffre, text='π', height=0, width=0,
                 command=lambda: ajoutpi(), padx=15, pady=5)

##########

boutonplus = Button(fenetre, font=police_chiffre, bg=fond_touche_opérateur,
                 fg=couleur_chiffre, text='+', height=0, width=0,
                 command=lambda: ajoutplus(), padx=15, pady=5)

boutonmoins = Button(fenetre, font=police_chiffre, bg=fond_touche_opérateur,
                 fg=couleur_chiffre, text='-', height=0, width=0,
                 command=lambda: ajoutmoins(), padx=15, pady=5)

boutonfois = Button(fenetre, font=police_chiffre, bg=fond_touche_opérateur,
                 fg=couleur_chiffre, text='x', height=0, width=0,
                 command=lambda: ajoutfois(), padx=15, pady=5)

boutondiviser = Button(fenetre, font=police_chiffre, bg=fond_touche_opérateur,
                 fg=couleur_chiffre, text='÷', height=0, width=0,
                 command=lambda: ajoutdiviser(), padx=15, pady=5)
boutonvirgule = Button(fenetre, font=police_chiffre, bg=fond_touche_opérateur,
                 fg=couleur_chiffre, text=',', height=0, width=0,
                 command=lambda: ajoutvirgule(), padx=15, pady=5)

boutonegal = Button(fenetre, font=police_chiffre, bg=fond_touche_opérateur,
                 fg=couleur_chiffre, text='=', height=0, width=0,
                 command=lambda: ajoutegal(), padx=15, pady=5)

boutonreset = Button(fenetre, font=police_chiffre, bg=fond_touche_opérateur,
                 fg=couleur_chiffre, text='C', height=0, width=0,
                 command=lambda: reset(), padx=15, pady=5)


bouton1_fenetre = canvas.create_window(50, 250, window=bouton1)
bouton2_fenetre = canvas.create_window(150, 250, window=bouton2)
bouton3_fenetre = canvas.create_window(250, 250, window=bouton3)
bouton4_fenetre = canvas.create_window(50, 350, window=bouton4)
bouton5_fenetre = canvas.create_window(150, 350, window=bouton5)
bouton6_fenetre = canvas.create_window(250, 350, window=bouton6)
bouton7_fenetre = canvas.create_window(50, 450, window=bouton7)
bouton8_fenetre = canvas.create_window(150, 450, window=bouton8)
bouton9_fenetre = canvas.create_window(250, 450, window=bouton9)
bouton0_fenetre = canvas.create_window(150, 550, window=bouton0)
boutonpi_fenetre = canvas.create_window(50, 50, window=boutonpi)

boutonplus_fenetre = canvas.create_window(350, 250, window=boutonplus)
boutonmoins_fenetre = canvas.create_window(350, 350, window=boutonmoins)
boutonfois_fenetre = canvas.create_window(350, 450, window=boutonfois)
boutondiviser_fenetre = canvas.create_window(250, 550, window=boutondiviser)
boutonegal_fenetre = canvas.create_window(50, 550, window=boutonvirgule)
boutonegal_fenetre = canvas.create_window(350, 550, window=boutonegal)
boutonreset_fenetre = canvas.create_window(350, 50, window=boutonreset)

Visuel_fenetre = canvas.create_window(200, 150, width = 400, height = 100, window=Visuel)

##########################################



##########################################

D = decimal.Decimal

compteur = 0
compteur_virgule = 0
variable = 0
variable1 = 0
var_plus = 0
var_moins = 0
var_fois = 0
var_diviser = 0
var_stock = 0
easter_egg = 0
var_pi = 0


def ajoutpi():
    global resultat, compteur_virgule, var_pi
    if compteur_virgule == 0 :
        resultat = pi
        var_pi = 1
        ajoutresultat("π")

def ajout1():
    global resultat, compteur_virgule
    if compteur_virgule == 1 :
        resultat2 = int(resultat)
        resultat2 = str(resultat2)
        resultat = resultat2 + ".1"
        compteur_virgule = 0
        ajoutresultat(resultat)
    else :
        resultat += "1"
        ajoutresultat(resultat)

def ajout2():
    global resultat, compteur_virgule
    if compteur_virgule == 1 :
        resultat2 = int(resultat)
        resultat2 = str(resultat2)
        resultat = resultat2 + ".2"
        compteur_virgule = 0
        ajoutresultat(resultat)
    else :
        resultat += "2"
        ajoutresultat(resultat)
    
def ajout3():
    global resultat, compteur_virgule
    if compteur_virgule == 1 :
        resultat2 = int(resultat)
        resultat2 = str(resultat2)
        resultat = resultat2 + ".3"
        compteur_virgule = 0
        ajoutresultat(resultat)
    else :
        resultat += "3"
        ajoutresultat(resultat)

def ajout4():
    global resultat, compteur_virgule
    if compteur_virgule == 1 :
        resultat2 = int(resultat)
        resultat2 = str(resultat2)
        resultat = resultat2 + ".4"
        compteur_virgule = 0
        ajoutresultat(resultat)
    else :
        resultat += "4"
        ajoutresultat(resultat)

def ajout5():
    global resultat, compteur_virgule
    if compteur_virgule == 1 :
        resultat2 = int(resultat)
        resultat2 = str(resultat2)
        resultat = resultat2 + ".5"
        compteur_virgule = 0
        ajoutresultat(resultat)
    else :
        resultat += "5"
        ajoutresultat(resultat)
    
def ajout6():
    global resultat, compteur_virgule
    if compteur_virgule == 1 :
        resultat2 = int(resultat)
        resultat2 = str(resultat2)
        resultat = resultat2 + ".6"
        compteur_virgule = 0
        ajoutresultat(resultat)
    else :
        resultat += "6"
        ajoutresultat(resultat)
    
def ajout7():
    global resultat, compteur_virgule
    if compteur_virgule == 1 :
        resultat2 = int(resultat)
        resultat2 = str(resultat2)
        resultat = resultat2 + ".7"
        compteur_virgule = 0
        ajoutresultat(resultat)
    else :
        resultat += "7"
        ajoutresultat(resultat)
    
def ajout8():
    global resultat, compteur_virgule
    if compteur_virgule == 1 :
        resultat2 = int(resultat)
        resultat2 = str(resultat2)
        resultat = resultat2 + ".8"
        compteur_virgule = 0
        ajoutresultat(resultat)
    else :
        resultat += "8"
        ajoutresultat(resultat)
    
def ajout9():
    global resultat, compteur_virgule
    if compteur_virgule == 1 :
        resultat2 = int(resultat)
        resultat2 = str(resultat2)
        resultat = resultat2 + ".9"
        compteur_virgule = 0
        ajoutresultat(resultat)
    else :
        resultat += "9"
        ajoutresultat(resultat)
    
def ajout0():
    global resultat, compteur_virgule
    if compteur_virgule == 1 :
        resultat2 = int(resultat)
        resultat2 = str(resultat2)
        resultat = resultat2 + ".0"
        compteur_virgule = 0
        ajoutresultat(resultat)
    else :
        resultat += "0"
        ajoutresultat(resultat)

def ajoutplus():
    global resultat, compteur, variable, variable1, var_plus, compteur_virgule, var_stock
    if var_plus == 1 :
        ajoutegal()
        compteur_virgule = 0
    if var_moins == 1 :
        ajoutegal()
        compteur_virgule = 0
    if var_fois == 1 :
        ajoutegal()
        compteur_virgule = 0
    if var_diviser == 1 :
        ajoutegal()
        compteur_virgule = 0
    variable = float(resultat)
    var_stock = variable
    #print("ici",variable)
    resultat = ""
    Visuel.config(text = "")
    var_plus += 1

def ajoutmoins():
    global resultat, compteur, variable, variable1, var_moins, compteur_virgule, var_stock
    if var_plus == 1 :
        ajoutegal()
        compteur_virgule = 0
    if var_moins == 1 :
        ajoutegal()
        compteur_virgule = 0
    if var_fois == 1 :
        ajoutegal()
        compteur_virgule = 0
    if var_diviser == 1 :
        ajoutegal()
        compteur_virgule = 0
    variable = float(resultat)
    var_stock = variable
    resultat = ""
    Visuel.config(text = "")
    var_moins += 1

def ajoutfois():
    global resultat, compteur, variable, variable1, var_fois, compteur_virgule, var_stock
    if var_plus == 1 :
        ajoutegal()
        compteur_virgule = 0
    if var_moins == 1 :
        ajoutegal()
        compteur_virgule = 0
    if var_fois == 1 :
        ajoutegal()
        compteur_virgule = 0
    if var_diviser == 1 :
        ajoutegal()
        compteur_virgule = 0
    variable = float(resultat)
    var_stock = variable
    resultat = ""
    Visuel.config(text = "")
    var_fois += 1

def ajoutdiviser():
    global resultat, compteur, variable, variable1, var_diviser, compteur_virgule, var_stock
    if var_plus == 1 :
        ajoutegal()
        compteur_virgule = 0
    if var_moins == 1 :
        ajoutegal()
        compteur_virgule = 0
    if var_fois == 1 :
        ajoutegal()
        compteur_virgule = 0
    if var_diviser == 1 :
        ajoutegal()
        compteur_virgule = 0
    variable = float(resultat)
    var_stock = variable
    resultat = ""
    Visuel.config(text = "")
    var_diviser += 1

def ajoutegal():
    global resultat, variable, variable1, var_plus, var_moins, var_fois, var_diviser, compteur_virgule, var_stock, easter_egg
    """print("resultat = ", resultat)
    print(type(resultat))"""
    variable1 = float(resultat)
    """print("variable1 = ",variable1)"""
    variable = var_stock
    """print("variable = ",variable)"""
    if var_plus == 1 :
        """print(float(variable))
        print(float(variable1))
        print(float(variable + variable1))"""
        resultat = D(str(variable)) + D(str(variable1))
        var_plus = 0
        compteur_virgule = 0
    if var_moins == 1 :
        resultat = D(str(variable)) - D(str(variable1))
        var_moins = 0
        compteur_virgule = 0
    if var_diviser == 1 :
        resultat = D(str(variable)) / D(str(variable1))
        var_diviser = 0
        compteur_virgule = 0
    if var_fois == 1 :
        resultat = D(str(variable)) * D(str(variable1))
        var_fois = 0
        compteur_virgule = 0
    if resultat == str(301204) :
        ajoutresultat(resultat)
        easter_egg += 1
    ajoutresultat(resultat)

def ajoutresultat(resultat):
    global easter_egg, var_pi
    if var_pi == 1:
        Visuel.config(text = resultat)
        #print("oui")
    if easter_egg == 1 :
        easter_egg = 0
        Visuel.config(text = "UWU")
    else :
        if var_pi == 0 :
            Visuel.config(text = float(resultat))
    var_pi = 0

def ajoutvirgule():
    global compteur_virgule, variable
    if compteur_virgule == 0 :
        variable = float(resultat)
        #print(float(variable))
        variable = str(variable)
        #print(str(variable))
        """variable += "."""
        #print(str(variable))
        compteur_virgule += 1

def reset():
    global resultat, variable, variable1, var_plus, var_moins, var_fois, var_diviser, compteur_virgule
    resultat = ""
    variable = 0
    variable1 = 0
    var_plus = 0
    var_moins = 0
    var_fois = 0
    var_diviser = 0
    compteur_virgule = 0
    Visuel.config(text = "")

##########################################
fenetre.mainloop()
