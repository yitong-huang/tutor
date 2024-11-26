import participant
import random
import time


# Unit setup
def unitSetup(player, ai):
    player.unitsSetup()
    ai.unitsSetup()


# Ask player whether use coin
def useCoin(participant):
    return participant.useCoin()


# Print state
def printState(player, ai):
    print()
    print("Coins:", player.getCoin())
    print("Number", "Name", "Profession", " Hp", "Atk", "Def", "Exp", "Rank", sep='\t')

    # Print player unit attribute
    i = 1
    for unit in player.getUnits():
        print(i, unit, sep='\t')
        i += 1

    # Separator
    print("--------------------------------------------------------------------")

    # Print AI unit attribute
    i = 1
    for unit in ai.getUnits():
        print(i, unit, sep='\t')
        i += 1
    print()


# wait x seconds for update
def waitFewSec(seconds):
    print()
    for i in range(seconds):
        print("Update in", 3 - i, "seconds.")
        time.sleep(1)


# Check whether the unit can level up
def levelUp(unit):
    if unit.getExp() >= 100:
        unit.levelUp()


# Fighting
def fighting(attacker, target, gameLog):
    # Calculate damage and update hp and exp
    damage = attacker.damage(target)

    # Display the battle detail
    print()
    print(attacker.getGroup() + "'s unit " + attacker.getName() + " attacked " + target.getName())
    print(target.getGroup() + "'s unit " + target.getName() + " takes " + str(damage) + " damage")

    # Record the game event
    gameLog.write(time.asctime() + ":\n")
    gameLog.write(
        "----" + attacker.getGroup() + "'s unit " + attacker.getName() + " attacked " + target.getName() + "\n")
    gameLog.write(
        "----" + target.getGroup() + "'s unit " + target.getName() + " takes " + str(damage) + " damage" + "\n\n")

    # Check whether attacker can level up
    levelUp(attacker)

    # Check whether target is alive
    if target.getCurrentHp() > 0:
        # If target is alive, check whether it can level up
        levelUp(target)

    return damage


# Check whether the unit is dead
def dead(participants, gameLog):
    for participant in participants:
        for unit in participant.getUnits():
            if unit.getCurrentHp() <= 0:
                print(str(participant) + "'s unit " + unit.getName() + " is dead")
                gameLog.write(
                    time.asctime() + ":\n----" + str(participant) + "'s unit " + unit.getName() + " is dead\n\n")
                participant.getUnits().remove(unit)


def main():
    # Ask Player start or exit
    gameStart = input("Start game?[y/n]:")

    if gameStart == 'y':
        # Create game log
        gameLog = open('gameLog.txt', 'w')

        print('Game started')
        gameLog.write(time.asctime() + ":\n----Game Start\n\n")

        # Create player, AI and reset game round
        player = participant.Participant("player", 3)
        ai = participant.Participant("AI", 3)
        gameRound = 0

        # Setup player units and ai units
        unitSetup(player, ai)

        # Game started
        while True:
            gameRound += 1

            # Print the round and state of units
            print("Round", gameRound)
            gameLog.write(time.asctime() + ":\n----Round: " + str(gameRound) + "\n\n")
            printState(player, ai)

            # Check round is even or odd
            if gameRound % 2 == 1:  # Odd game round (player's round)

                if player.getCoin() >= 200:
                    healUnit = useCoin(player)
                    if healUnit != False:
                        print("Player has heal " + healUnit + "\n")
                        gameLog.write(time.asctime() + ":\n----Player has heal " + healUnit + "\n\n")
                        continue

                # Get valid attacker's number and check whether player want to quit
                atkNum = player.getAtkNum()
                if atkNum == 'q':
                    gameLog.write(time.asctime() + ":\n----Player quit the game\n\n")
                    break

                # Get valid target's number and check whether player want to quit
                targetNum = player.getTargetNum(ai)
                if targetNum == 'q':
                    gameLog.write(time.asctime() + ":\n----Player quit the game\n\n")
                    break

                # Start fighting
                player.addCoin(fighting(player.getUnit(atkNum), ai.getUnit(targetNum), gameLog))

            else:
                # Even game round (AI's round)

                # Randomly select attacker and target
                atkNum = random.randint(0, len(ai.getUnits()) - 1)
                targetNum = random.randint(0, len(player.getUnits()) - 1)

                # Start fighting
                fighting(ai.getUnit(atkNum), player.getUnit(targetNum), gameLog)

            dead([player, ai], gameLog)
            # Wait 3 seconds for update
            waitFewSec(3)
            print()

            # Check whether both sides are alive
            if len(player.getUnits()) == 0:
                printState(player, ai)
                print("Game over, you lose")
                gameLog.write(time.asctime() + ":\n----AI win\n\n")
                break
            elif len(ai.getUnits()) == 0:
                printState(player, ai)
                print("Congratulation, you win")
                gameLog.write(time.asctime() + ":\n----Player win\n\n")
                break

        gameLog.write(time.asctime() + ":\n----Game End\n")
        gameLog.close()
        print("Thanks for playing")

    else:
        print('exit')


if __name__ == "__main__":
    main()
