import unit
import random
from profession import *


class Participant:

    # Initializes all the attribute of a player
    def __init__(self, participantType, amount):
        self.__name = ''
        self.__participantType = participantType
        self.__coin = 0
        self.__units = []
        self.__unitsAmount = amount
        if participantType == 'player':
            self.__exp = 0
            self.__rank = 1
        
            

    # Set name, get name
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name


    # Set participant type, get participant type
    def setParticipantType(self, participantType):
        self.__participantType = participantType

    def getParticipantType(self):
        return self.__participantType

    # Set coin, add coin, get coin
    def setCoin(self, coin):
        self.__coin = coin

    def addCoin(self, amount):
        self.__coin += amount

    def useCoin(self):
        defaultHeal = 30
        choice = input("Do you wish to use coin for healing unit? [y/n]:")
        if choice == 'y':
            while True:
                target = input("Choose the unit you wish to heal:")
                if target.isdigit() and int(target) in self.getUnitsNum():
                    self.__units[int(target)-1].heal(defaultHeal)
                    self.__coin -= 200
                    break
                else:
                    print("ERROR: invalid value")
            return self.__units[int(target)-1].getName()
        else:
            return False
        
            

    def getCoin(self):
        return self.__coin


    # Set units, units setup, del unit, get units, get units num, get unit
    def setUnits(self, units):
        self.__units = units

    def unitsSetup(self):

        if self.__participantType == 'player':
            # Ask player type name
            for i in range(self.__unitsAmount):
                unitName = input("Please name unit "+str(i+1)+":")
                while True:
                    profession = input("Enter the profession for unit "+str(i+1)+" [w(for warrior)/t(for tanker)]:")
                    if profession.lower() == 'w':
                        self.__units.append(unit.Unit(unitName, Profession.WARRIOR))
                        self.__units[i].setupWarrior()
                        break
                    elif profession.lower() == 't':
                        self.__units.append(unit.Unit(unitName, Profession.TANKER))
                        self.__units[i].setupTanker()
                        break
                    else:
                        print("Please enter w or t for profession")
                    
                    
                self.__units[i].setGroup(self.__participantType)
                print()

        else:
            for i in range(self.__unitsAmount):
                
                unitName = 'AI'+str(random.randint(0,9))+str(random.randint(0,9))
                profession = ''
                if random.randint(0,1) == 0:
                    self.__units.append(unit.Unit(unitName, Profession.WARRIOR))
                    self.__units[i].setupWarrior()
                else:
                    self.__units.append(unit.Unit(unitName, Profession.TANKER))
                    self.__units[i].setupTanker()
                self.__units[i].setGroup(self.__participantType)


    def delUnit(self, index):
        del self.__units[index]

    def getUnits(self):
        return self.__units

    def getUnitsNum(self):
        list1 = []
        for i in range(len(self.__units)):
            list1.append(i+1)
        return list1

    def getUnit(self, index):
        return self.__units[index]

    # Set units amount, get units amount
    def setUnitsAmount(self, amount):
        self.__unitsAmount = amount

    def getUnitsAmount(self):
        return self.__unitsAmount


    # Set exp, add exp, get exp
    def setExp(self, exp):
        self.__exp = exp

    def addExp(self,amount):
        self.__exp += amount
    
    def getExp(self):
        return self.__exp

    # Set rank, get rank
    def setRank(self, rank):
        self.__rank = rank

    def levelUp(self):
        self.__exp -= 100
        self.__rank += 1

    def getRank(self):
        return self.__rank


    # Ask player type attacker's number
    def getAtkNum(self):
        while True:
            atkNum = input("Enter a attacker's number [1-"+str(len(self.__units))+"]/q(for quit):")

            if atkNum == 'q':   # If input is 'q' then quit the game
                return atkNum
            elif atkNum.isdigit() and int(atkNum) in self.getUnitsNum():
                # Change atkNum to integer
                atkNum = int(atkNum)-1
                return atkNum
            else:
                print("Error: invalid value")
                print()

    # Ask player type target's number
    def getTargetNum(self, ai):
        while True:
            targetNum = input("Enter a target's number you want to attack [1-"+str(len(ai.getUnits()))+"]/q(for quit):")

            if targetNum == 'q':   # If input is 'q' then quit the game
                return targetNum
            elif targetNum.isdigit() and int(targetNum) in ai.getUnitsNum():
                # Change targetNum to integer
                targetNum = int(targetNum)-1
                return targetNum
            else:
                print("Error: invalid value")
                print()


    # Display the participant type
    def __str__(self):
        return self.__participantType



