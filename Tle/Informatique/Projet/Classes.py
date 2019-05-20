class Joueur:
    x = 0
    y = 0
    tr_x = 0
    tr_y = 0
    frame = [0,0]
    moving = False
    
    sac = []
    maxSac = 15
    
    def __repr__(self):
        return 'x(%s,%s) y(%s,%s) sac(%s/%s)' % (self.x,self.tr_x , self.y,self.tr_y , self.sac,self.maxSac)
    
    def bouge(self,mv_x,mv_y):
        self.x += mv_x
        self.y += mv_y
        self.tr_x = -mv_x*16
        self.tr_y = -mv_y*12
    
    def routine(self):
        #déplacement
        if self.tr_x>0: self.tr_x -= 1
        if self.tr_x<0: self.tr_x += 1
        if self.tr_y>0: self.tr_y -= 0.75
        if self.tr_y<0: self.tr_y += 0.75

class Niveau:
    sol = []        #Les zones où on peut marcher (nombres). 0 = mur ; 1 = sol ; 2 = entrée (sol)
    coffres = []    #Les coffres, par id (nombres)
    contenu = []    #Le contenu et l'apparence de chaque coffre, identifié par son id (dictionnaire {"id":[liste]} )
    start = []      #Le point de départ
    time = int()    #Le temps imparti, en secondes
    
    def __init__(self,fichier):
        with open(fichier, 'r') as f:
            text = ""
            for x in range(16):
                fr = f.readline()
                text += fr
            self.sol = eval(text)
            text = ""
            for x in range(16):
                fr = f.readline()
                text += fr
            self.coffres = eval(text)
            text = ""
            while True:
                fr = f.readline()
                if fr=="STOP\n":
                    break
                text += fr
            self.contenu = eval(text)
            fr = f.readline()
            self.start = eval(fr)
            fr = f.readline()
            self.time = eval(fr)
    
    def __repr__(self):
        return 'sol\n%s\ncoffres\n%s\ncontenu\n%s' % (self.sol,self.coffres,self.contenu)
    
    def depart(self,joueur,temps):
        if type(joueur) != Joueur: raise Exception("joueur est du type %s au lieu de Joueur"
                                                    % (type(joueur)))
        
        x , y = self.start[0] , self.start[1]
        joueur.x = x
        joueur.y = y
        temps = self.time*60
        return (x,y)
        
