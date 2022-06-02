import random
playerHistory = []
cpuHistory = []
playAgain = True
howManyTimesHasCPUWon = 0
totalGamesPlayed = 0
RPSList = ["R", "P", "S"]
def did_the_player_win_the_round(playerNum, cpuNum):
    cpuWins = False #bc the player lost
    playerWins = True #bc the player did win
    if playerNum==cpuNum:
        return "Tie"
    else:
        if (playerNum - 1)%3 == cpuNum:
            return playerWins
        else:
            return cpuWins 

def get_cpu_move():
    #In the future this is where machine learning stuff will go
    return random.randint(0, 2) 

def move_to_number(str1):
    if str1 in RPSList:
        return RPSList.index(str1)
    else: 
        return -1

print("Type \"R\" for rock, \"P\" for paper or \"S\" for scissors, followed by the enter key.\nOr if you want to quit, type \"Q\".")
while(playAgain):
    playerMove=input("")
    playerMove = playerMove.upper()
    if playerMove == "Q":
        print("Thanks for playing!")
        break
    else:
        playerMove = move_to_number(playerMove)
        if playerMove==-1: #they didn't type R, p, or s
            print("Please type a valid response.")
            continue
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

        
