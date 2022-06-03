import random
import tkinter as tk
from tkinter import ttk

"""
Initialize our global variables
"""

"""
This tracks how many times each possible game has been played. There are nine possible outcomes,
and we start out with each game set to 0. Once a game is played, we increase it's count by 1
"""
# gameHistory = {
#     (0,0): 0,
#     (0,1): 0,
#     (0,2): 0,
#     (1,0): 0,
#     (1,1): 0,
#     (1,2): 0,
#     (2,0): 0,
#     (2,1): 0,
#     (2,2): 0
# }


"""
Our prediction is a disct with 9 keys representing the 9 possible outcomes of player v computer
the value of each key is itself a dict with 3 keys, representing players next move and the number of times we've seen it. 
It starts out with every cell = 0 since the player hasn't made a move yet
But this will update over time
"""
prediction = gameHistory = {
    (0,0): {0: 0, 1: 0, 2: 0},
    (0,1): {0: 0, 1: 0, 2: 0},
    (0,2): {0: 0, 1: 0, 2: 0},
    (1,0): {0: 0, 1: 0, 2: 0},
    (1,1): {0: 0, 1: 0, 2: 0},
    (1,2): {0: 0, 1: 0, 2: 0},
    (2,0): {0: 0, 1: 0, 2: 0},
    (2,1): {0: 0, 1: 0, 2: 0},
    (2,2): {0: 0, 1: 0, 2: 0}
}

prevGame =""
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
    if prevGame=="": #if it's game 1
        return random.randint(0,2)
    
    #we'll look at the dict stored in the prediction dict at the previous move key. 
    possibleMoves = prediction[prevGame]

    #From there we see what move the player made historically, and predict that the player will make the move (s)he's made most often in the past
    values = possibleMoves.values()
    maximum = max(values)
    for key in possibleMoves.keys():
        if possibleMoves[key] == maximum:
            ourGuess = key

    #and then we beat 'em
    return (ourGuess+1)%3
def move_to_number(str1):
    if str1 in RPSList:
        return RPSList.index(str1)
    else:
        return -1

def playTheGame(playerMove):
    global totalGamesPlayed
    totalGamesPlayed += 1
    cpuMove = get_cpu_move()
    global prevGame
    if prevGame != "":
        prediction[prevGame][playerMove] = prediction[prevGame][playerMove]+1 #we add one to the number of times player has responded with their choice of move based on the previous game
    prevGame = (playerMove, cpuMove)
    
    
    
    playerWonTheRound = did_the_player_win_the_round(playerMove, cpuMove)
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