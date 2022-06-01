import random
playerHistory = []
cpuHistory = []
playAgain = True
howManyTimesHasCPUWon = 0
totalGamesPlayed =0 
def did_the_player_win_the_round(str1, str2):
    cpuWins = False #bc the player lost
    playerWins = True #bc the player did win
    if str1==str2:
        return "Tie"
    else:
        if str1=="R":
            if str2 == "P":
                return cpuWins
            else: #str2==S
                return playerWins

        elif str1=="P":
            if str2 == "S":
                return cpuWins
            else:
                return playerWins

        else: #str1 == "S"
            if str2=="R":
                return cpuWins
            else:
                return playerWins

def get_cpu_move():
    #In the future this is where machine learning stuff will go
    move = random.randint(0, 3)
    if move==0:
        return "R"
    elif move==1:
        return "P"
    else:
        return "S"


print("Type \"R\" for rock, \"P\" for paper or \"S\" for scissors, followed by the enter key.\nOr if you want to quit, type \"Q\".")
while(playAgain):
    playerMove=input("")
    playerMove = playerMove.upper()
    if playerMove == "Q":
        print("Thanks for playing!")
        break
    elif playerMove == "R" or playerMove == "P" or playerMove == "S":
        totalGamesPlayed+=1
        cpuMove = get_cpu_move()
        cpuHistory.append(cpuMove)
        playerHistory.append(playerMove)
        playerWonTheRound = did_the_player_win_the_round(playerHistory[-1], cpuHistory[-1])

        if playerWonTheRound == "Tie":
            print("We had a tie. Let's play again.\n")
            continue
        elif(playerWonTheRound):
            print("You won this round. (╯°□°）╯︵ ┻━┻\n")
        else: #cpu won the round
            howManyTimesHasCPUWon +=1
            if howManyTimesHasCPUWon==1:
                print("I win this time :)\n")
            else:
                print("I win this round\n( ˘ ͜ʖ ˘)\nI've already won {} rounds so far.".format(howManyTimesHasCPUWon))
                cpuWinRate = round(float(howManyTimesHasCPUWon)/totalGamesPlayed*100, 2)
                print("In fact, I've won {}% of the games we've played so far.\n".format(cpuWinRate))

    else:
        print("Please type a valid response.")
        continue

