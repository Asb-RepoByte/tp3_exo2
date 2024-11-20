from Class_Vaisseau import Vaisseau

class jeu():
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.score = 0
        self.vies = 3
        self.fenetre.bouton1.config(text = 'Demarrer', command = self.start_game)
        self.aliens = []
        self.projectiles = []
        
    def start_game(self):
        self.vaisseau = Vaisseau(self,self.fenetre)