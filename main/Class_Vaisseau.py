from tkinter import *

class Vaisseau():
    def __init__(self, jeu, fenetre):
        self.jeu = jeu
        self.fenetre = fenetre
        self.posx = 300
        self.posy = 350
        self.image_vaisseau = PhotoImage(file = 'joueur.gif')
        self.vaisseau_id = self.jeu.fenetre.canvas.create_image(self.posx, self.posy, anchor = 'center',image = self.image_vaisseau)
        self.jeu.fenetre.canvas.bind('<Key>', self.deplacer_vaisseau)
    
    def deplacer_vaisseau(self, event):
        touche = event.keysym
        print(touche)
        if touche == 'Right':
            self.posx += 10
            if self.posx > 590: 
                self.posx = 590
        
        if touche  == 'Left':
            self.posx -= 10
            if self.posx < 10:
                self.posx = 10
        
        self.jeu.fenetre.canvas.coords(self.vaisseau_id, self.posx, self.posy)
        