
from tkinter import *

largeur_alien = 22      
hauteur_alien = 16
ecart_alien = 10
hauteur_alien_ligne1 = 50
nbre_alien_par_ligne = 15
descente_alien = 10
VitesseDeplacement = 10
VitesseAlien = 0.5
class Alien():
    Compteur = 0
    def __init__(self, fenetre):
        self.Compteur += 1
        self.Compteur = self.Compteur
        self.vivant = True
        self.x = self.Compteur*(ecart_alien + largeur_alien)
        self.y = hauteur_alien_ligne1
        self.dir = 1
        self.vitesse = VitesseAlien
        self.fenetre = fenetre
        self.Creation()
        self.Affichage()
        self.deplacer()
        self.descendre()
        #self.deplacer_aliens()
    def Creation(self):
        self.image_alien = PhotoImage(file = 'alien.gif')
        self.apparence = self.fenetre.canvas.create_image(300, 300, anchor = 'nw', image = self.image_alien)
        
    def Affichage(self):
        self.fenetre.canvas.coords(self.apparence,self.x,self.y)
    
    def deplacer(self):
        self.x += self.dir * self.vitesse
        if self.x > self.fenetre.Largeur - largeur_alien or self.x < 0:
            self.dir *= -1
            self.descendre()

    
    def descendre(self):
        self.y += descente_alien
        self.Affichage()
        

""" 
    def deplacer_aliens(self):
        self.aliens = []
        for i in range(nbre_alien_par_ligne):
            for j in range(4):
                x = i * (ecart_alien + largeur_alien)
                y = j * (ecart_alien + hauteur_alien)
                self.alien = Alien(self,x , y)
                self.aliens.append(alien)
        
        for alien in self.aliens:
            self.alien.deplacer()
    
        for alien in self.aliens:
            if self.alien.x > 800 - largeur_alien or alien.x < 0:
                for alien in self.aliens:
                    self.alien.descendre()
                break
        
        self.fenetre.after(int(VitesseDeplacement), self.deplacer_aliens)
        
"""