import random
from profession import *

# Extra exp rate
EXTRAEXP1 = 1.2
EXTRAEXP2 = 1.5


class Unit:

    # Initializes all the attribute of a unit
    def __init__(self):
        self.__name = ''
        self.__profession = Profession.UNKNOWN
        self.__maxHp = 100
        self.__currentHp = 100
        self.__attack = 0
        self.__defence = 0
        self.__exp = 0
        self.__rank = 1
        self.__group = ''

    def __init__(self, name, profession):
        self.__name = name
        self.__profession = profession
        self.__maxHp = 100
        self.__currentHp = 100
        self.__attack = 0
        self.__defence = 0
        self.__exp = 0
        self.__rank = 1
        self.__group = ''

    # Set name, get name
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    # Set profession, get profession, setup warrior, setup tanker
    def setProfession(self, profession):
        self.__profession = profession
        self.initAtkDef()

    def getProfession(self):
        return self.__profession

    def setupWarrior(self):
        self.__attack = random.randint(5, 20)
        self.__defence = random.randint(1, 10)

    def setupTanker(self):
        self.__attack = random.randint(1, 10)
        self.__defence = random.randint(5, 15)

    # Set max hp, get max hp
    def setMaxHp(self, maxHp):
        self.__maxHp = maxHp

    def getMaxHp(self):
        return self.__maxHp

    # Set current hp, take damage, healing, get current hp
    def setCurrentHp(self, currentHp):
        self.__currentHp = currentHp

    def damage(self, target):
        # Calculate the damage and update hp
        damage = self.__attack - target.__defence + random.randint(-5, 10)
        target.__currentHp -= damage
        if target.__currentHp > target.__maxHp:
            target.__currentHp = target.__maxHp

        # Update exp
        self.__exp += damage
        if self.__exp < 0:
            self.__exp = 0
        if damage > 10:
            target.__exp += int(target.__defence * EXTRAEXP1)
        elif damage <= 0:
            target.__exp += int(target.__defence * EXTRAEXP2)
        else:
            target.__exp += target.__defence

        return damage

    def heal(self, healing):
        self.__currentHp += healing
        if self.__currentHp > self.__maxHp:
            self.__currentHp = self.__maxHp

    def getCurrentHp(self):
        return self.__currentHp

    # Set attack ,get attack
    def setAttack(self, attack):
        self.__attack = attack

    def getAttack(self):
        return self.__attack

    # Set defence, get defence
    def setDefence(self, defence):
        self.__defence = defence

    def getDefence(self):
        return self.__defence

    # Set exp, add exp, get exp
    def setExp(self, exp):
        self.__exp = exp

    def addExp(self, amount):
        self.__exp += amount

    def getExp(self):
        return self.__exp

    # Set rank, get rank
    def setRank(self, rank):
        self.__rank = rank

    def levelUp(self):
        self.__exp -= 100
        self.__rank += 1
        if self.__profession == Profession.WARRIOR:
            self.__attack += 2
            self.__maxHp += 5
        else:
            self.__defence += 1
            self.__maxHp += 7

    def getRank(self):
        return self.__rank

    # Set group, get group
    def setGroup(self, group):
        self.__group = group

    def getGroup(self):
        return self.__group

    # Display the state of an unit
    def __str__(self):
        string = "{}\t{}  \t {}\t{}\t{}\t{}\t{}"
        string = string.format(self.__name, self.__profession, self.__currentHp, self.__attack, self.__defence,
                               self.__exp, self.__rank)
        return string
