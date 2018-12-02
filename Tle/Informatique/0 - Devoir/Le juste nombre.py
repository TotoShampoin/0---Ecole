from random import randint
num = randint(1,100)
guess = 0
count = 0
print("Le jeu consiste a deviner un nombre entre 1 et 100:")
while(guess!=num):
    count+=1
    guess = int(input("--->  "))
    if(guess==num):
        print("Gagne en ", count, " coups !", flush=True)
    else:
        if(guess>num):
            print("Trop grand !")
        else:
            print("Trop petit !")
