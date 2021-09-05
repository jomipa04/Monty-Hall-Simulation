import random
W=0
L=0

def Monty():
    res = ''
    choice = ["goat", "goat", "goat"]
    goat=[]
    positions=[]
    initial_choice =0
    car_pos =0

#assign choice and car position
    for h in range(2):
        if h==0:
            initial_choice=random.randint(0,2)
           
        else:
            car_pos=random.randint(0,2)
           

#assign car
    choice[car_pos]="car"
    

#goat list
    for i in range(3):
        if choice[i]== "goat":
            goat.append(i)
   


#reveal goat
    if goat[0]==initial_choice:
        reveal_goat = goat[1]
    else:
        reveal_goat = goat[0]
    

#two choices
    two_choice =[0,1,2]
    for k in range(3):
        if reveal_goat== k:
            two_choice.remove(k)

   

#switch choice
    for m in range(2):
        if initial_choice != two_choice[m]:
            initial_choice = two_choice[m]
            break
    if choice[initial_choice]=="car":
        res = 'Win'
    else:
        res = 'Lose'

    return res

for z in range(100):
    for i in range(100):
        result=Monty()
        if result == 'Win':
            W+=1
        else:
            L+=1
    
    print()
    print("Wins:", W)
    print("Lose:", L)
    W=0
    L=0
