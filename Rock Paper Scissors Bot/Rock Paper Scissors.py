import random
import tkinter as tk
from tkinter import ttk

"""
Initialize our global variables
"""
playerHistory = []
cpuHistory = []
playAgain = True
howManyTimesHasCPUWon = 0
totalGamesPlayed = 0
RPSList = ["R", "P", "S"]


"""
Initialize our gui
"""





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

def playTheGame(playerMove):
    #playerMove = move_to_number(playerMove) We can just pass 0, 1, or 2 from the button
    global totalGamesPlayed
    totalGamesPlayed += 1
    cpuMove = get_cpu_move()
    cpuHistory.append(cpuMove)
    playerHistory.append(playerMove)
    playerWonTheRound = did_the_player_win_the_round(playerHistory[-1], cpuHistory[-1])

    if playerWonTheRound == "Tie":
        result = "We had a tie. Let's play again."


    elif(playerWonTheRound):
        result = "You won this round. (╯°□°）╯︵ ┻━┻"
    else: #cpu won the round
        global howManyTimesHasCPUWon
        howManyTimesHasCPUWon += 1
        if howManyTimesHasCPUWon==1:
            result = "I win this time :)"
        else:
            cpuWinRate = round(float(howManyTimesHasCPUWon)/totalGamesPlayed*100, 2)
            result = "I win this round\n( ˘ ͜ʖ ˘)\nI've already won {} rounds so far.\nIn fact, I've won {}% of the games we've played so far.".format(howManyTimesHasCPUWon, cpuWinRate)

    result_label.config(text=result)
    print(result)




howToPlay = "Click on a button to make that move."
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry('600x400+50+50')
# frame
frame = ttk.Frame(root)
frame.pack()
button_frame = ttk.Frame(root)
button_frame.pack()
results_frame = ttk.Frame(root)
results_frame.pack()

# field options
options = {'padx': 5, 'pady': 5}



# add padding to the frame and show it
#frame.grid(padx=10, pady=10)

message = tk.Label(frame, text=howToPlay)
message.grid(column=3, row=0, columnspan=5)

rockbutton = ttk.Button(button_frame, text="Rock")
rockbutton.grid(column=3, row=1, padx=5)
rockbutton.configure(command=lambda: playTheGame(0))

paperButton = ttk.Button(button_frame, text = "Paper")
paperButton.grid(column=4, row=1, padx=5)
paperButton.configure(command=lambda: playTheGame(1))

scissorsButton = ttk.Button(button_frame, text = "Scissors")
scissorsButton.grid(column=5, row=1, padx=5)
scissorsButton.configure(command=lambda: playTheGame(2))

# result label
result_label = ttk.Label(results_frame)
result_label.grid(column = 5, row = 5, columnspan=10)
root.mainloop()