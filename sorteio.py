import random
import time
import os


def time_1():
    for cont in range(10,-1,-1):
        os.system("cls") 
        print(cont,' segundos')
        time.sleep(1)
   
    
os.system('cls')

print("X"*45)
print("X"*25)
print("X"*25)
print()
print()

parsas=['Nicolas','Felipe','Tiago','Elton','Evair','Brian', 'Shuel','juliano']
print()
print()
print("X"*45)
print("X"*45)
print()
print()
print(" Vamos ao Gamer, grite pelo seu nome!!!!!")
quarta_de_final = random.sample(parsas,3)
print()
print()
print("X"*45)
print("X"*45)
print()
print()

print("Sejam bem vindos jogadores", parsas)
print()
print( "                        la vem os semi-finalista: ")
time.sleep(10)

time_1()   

os.system('cls')

print(" parabéns",quarta_de_final, " vocês são os semi-finalista ")

time.sleep(10)
os.system('cls')
print()
print(quarta_de_final," vamos ao gamer,  grite pelo seu nome!!!!!")
print()
print("       **********  La vém os finalista!!  ****************** ")
time.sleep(10)
print()
semi_final = random.sample(quarta_de_final,2)

print("X" * 65)
print("X" * 65)
print()
print(" Parabéns ", semi_final, " vamos para a grande final!!")
print()
print("X" * 65)
print("X" * 65)
print()

print( "       **********",semi_final,"**********")
time.sleep(10)
os.system("cls")

final = random.sample(semi_final,1)
print()
print(" La vém o campeão!! ")
print()
time.sleep(10)
print("X" * 65)
print("X" * 65)
print()
print(" Parabéns ", final, "você é o campeão, seu premio é uma pizza!!")
print()
print("X" * 65)
print("X" * 65)
print()
print(" passe o seu pix")







