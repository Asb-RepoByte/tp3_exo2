from tkinter import *
from  Class_Fenetre import Fenetre
from Class_Alien import Alien 
from Class_jeu import jeu
from Class_Vaisseau import Vaisseau
Space_invaders = Tk()
Space_invaders.title("Space invaders")
mf = Fenetre(Space_invaders)
ma = Alien(mf)
mk = jeu(mf)
Space_invaders.mainloop()
