class Joueur:
    x = 0
    y = 0
    tr_x = 0
    tr_y = 0
    
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
        if self.tr_y>0: self.tr_y -= 1
        if self.tr_y<0: self.tr_y += 1

class Niveau:
    sol = []        #Les zones où on peut marcher (nombres). 0 = mur ; 1 = sol ; 2 = entrée (sol)
    coffres = []    #Les coffres, par id (nombres)
    contenu = []    #Le contenu et l'apparence de chaque coffre, identifié par son id (dictionnaire {"id":[liste]} )
    
    def __init__(self,fichier):
        with open(fichier, '') as f:
            text = ""
            for x in range(16):
                text += "\n"+f.readline()
            self.sol = eval(text)
            text = ""
            for x in range(16):
                text += "\n"+f.readline()
            self.coffres = eval(text)
            text = ""
            for x in range(16):
                text += "\n"+f.readline()
            self.contenu = eval(text)
    
    def depart(self,joueur):
        if type(joueur) != Joueur: raise Exception("joueur est du type %s au lieu de Joueur"
                                                    % (type(joueur)))
        for y in range(16):
            for x in range(16):
                if self.sol[x][y]==2:
                    joueur.x = x
                    joueur.y = y
                    return (x,y)
        
