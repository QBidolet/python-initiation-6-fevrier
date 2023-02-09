from tkinter import *
import sqlite3


def creer_database():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()
    # execution d'une requête SQL pour créer la base de donnée
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts(nom TEXT, telephone TEXT)")
    connection.commit()
    cursor.close()
    connection.close()


def inserer():
    # insertion dans une base de donnée
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO contacts values(?,?)",
                   (nom_var.get(), telephone_var.get()))
    connection.commit()
    cursor.close()
    connection.close()


def afficher():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts")
    for nom, telephone in cursor.fetchall():
        print(f"{nom} | {telephone}")
    cursor.close()
    connection.close()


def init():
    # création de la fenêtre
    fenetre = Tk()
    fenetre.geometry("410x450")
    fenetre.title("Catalogue")
    fenetre.configure(background="powder blue")
    nom_label = Label(fenetre, text="Nom : ")
    nom_label.place(x=0, y=0)

    telephone_label = Label(fenetre, text="Téléphone :")
    telephone_label.place(x=0, y=30)

    global nom_var
    global telephone_var
    nom_var, telephone_var = StringVar(), StringVar()

    nom_entry = Entry(fenetre, width=20,
                      textvar=nom_var)
    nom_entry.place(x=80, y=0)

    telephone_entry = Entry(fenetre, width=20,
                            textvar=telephone_var)
    telephone_entry.place(x=80, y=30)

    # bouton
    bouton_ajouter = Button(fenetre, text="Ajouter",
                            command=inserer)
    bouton_ajouter.place(x=80, y=100)

    bouton_afficher = Button(fenetre, text="Afficher",
                             command=afficher)
    bouton_afficher.place(x=150, y=100)

    fenetre.mainloop()


creer_database()
init()
