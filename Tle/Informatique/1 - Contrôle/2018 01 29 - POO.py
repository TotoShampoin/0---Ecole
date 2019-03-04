# -*- coding: utf-8 -*-
class Personnage(object):  
    def __init__(self,entreeNom,nbreDeVie):          ###  Exercice 1
        self.nom = entreeNom                           # Nom
        self.vie = nbreDeVie
        self.forc = 1                                  # Force
        self.endu = 1                                  # Endurance
        self.chan = 5                                  # Chance
        self.inte = 10                                 # Intelligence
        self.rapi = 7                                  # Rapidité
        self.arme = 4                                  # Point d'attaque
    def afficheCaracteristiques(self):
        print(self.nom+""" a : 
 une force de """+str(self.forc)+""",
 une endurance de """+str(self.endu)+""",
 une chance de """+str(self.chan)+""",
 une intelligence de """+str(self.inte)+""",
 une rapidité de """+str(self.rapi))
# Les """ indiquent au programme qu'il faut retenir le retour à la ligne
# (C'est pour aérer le code)
    def perdVie(self,perte):                         ###  Exercice 4
        self.vie -= perte
# a -= b  revient à mettre a = a-b
    def afficheVie(self):                            ###  Exercice 3
        print(self.nom+" a "+str(self.vie)+" points de vie")
    def afficheEtat(self):                           ###  Exercice 5
        if(self.vie==0):
            print(self.nom+" est mort")
        else:
            print(self.nom+" est encore en vie")
def attaque(attaquant,attaque):                      ###  Exercice 6
    print(attaquant.nom+" attaque "+attaque.nom)
    attaque.perdVie(attaquant.forc+attaquant.arme)
 # Le nombre de points de vie perdus dépend de l'arme et de la force du perso

gollum = Personnage("Gollum", 25)
gollum.arme = 0                             # gollum n'a pas d'arme
bilbo = Personnage("Bilbo Sacquet", 20)

# Début
bilbo.afficheVie()
gollum.afficheVie()

# Gollum attaque, à mains nues
attaque(gollum,bilbo)
bilbo.afficheVie()
gollum.afficheVie()

# Bilbo attaque, avec son arme
attaque(bilbo,gollum)
bilbo.afficheVie()
gollum.afficheVie()
