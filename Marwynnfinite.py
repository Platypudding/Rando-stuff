#Defines Marwynn's starting power
Power = int(input("Enter Marwynn's power: "))
#Number of times you go through the full tap and untap process
Untap = int(input("Enter times tapped: "))
#Amount of mana in the pool. Always starts at 0
ManaPool = 0

#This loop basically simulates the process of tapping Marwynn for her power value, and untapping her for 3 mana, leaving her in an untapped state
for x in range(Untap):  
    ManaPool = ManaPool + Power - 3
    Power = Power + 2
    
    #Below ensures that you don't get negative values for the amount of mana in pool, which can't go below 0 and offputs the ManaPool output by 2 if it does
    if ManaPool < 0:
        ManaPool = 0
 
print(Power)
print(ManaPool)
