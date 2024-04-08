from tkinter import*

root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")

frame1=Frame(root)
frame1.pack()
titlelabel=Label(frame1,text="Tic Tac Toe",font=("Arial",30),bg="blue",width=16)
titlelabel.grid(row=0,column=0)

optionFrame=Frame(root,bg="grey")
optionFrame.pack()

frame2=Frame(root,bg="violet")
frame2.pack()

board={1:" ",2:" ",3:" ",
       4:" ",5:" ",6:" ",
       7:" ",8:" ",9:" "}

turn="X"
game_end=False
mode="singlePlayer"

def changeTosinglePlayer():
    global mode
    mode="singlePlayer"
    singlePlayerButton["bg"]="lightgreen"
    multiPlayerButton["bg"]="lightpink"

def changeToMultiplayer():
    global mode 
    mode = "multiPlayer"
    multiPlayerButton["bg"] = "lightgreen"
    singlePlayerButton["bg"] = "lightgrey"

def upddateBoard():
    for key in board.keys():
        buttons[key-1]["text"]=board[key]

def checkWin(player):
    #rows
    if board[1]==board[2] and board[2]==board[3] and board[3]==player:
        return True
    
    elif board[4]==board[5] and board[4]==board[6] and board[6]==player:
        return True
    
    elif board[7]==board[8] and board[7]==board[9] and board[9]==player:
        return True
    
    #column
    elif board[1]==board[4] and board[4]==board[7] and board[7]==player:
        return True
    
    elif board[2]==board[5] and board[2]==board[8] and board[8]==player:
        return True
    
    elif board[3]==board[6] and board[6]==board[9] and board[9]==player:
        return True

    # diagonals
    elif board[1]==board[5] and board[5]==board[9] and board[9]==player:
        return True
    
    elif board[3]==board[5] and board[5]==board[7] and board[7]==player:
        return True


    return False

def checkDraw():
    for i in board.keys():
        if board[i]==" ":
            return False
        
    return True

def restartGame():
    global game_end
    game_end=False
    for button in buttons:
        button["text"]=" "

    for i in board.keys():
        board[i]=" "
    titlelabel=Label(frame1,text="Tic Tac Toe",font=("Arial",30),bg="orange",width=15)
    titlelabel.grid(row=0,column=0)

def minimax(board,isMaximizing):
    if checkWin("o"):
        return 1 
    
    if checkWin("x"):
        return -1
    
    if checkDraw():
        return 0
    
    if isMaximizing:
        bestScore = -100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "o"
                score = minimax(board , False) # minimax
                board[key] = " "
                if score > bestScore : 
                    bestScore = score 
        
        return bestScore
    
    else:
        bestScore = 100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "x"
                score = minimax(board , True) # minimax
                board[key] = " "
                if score < bestScore : 
                    bestScore = score 
        
        return bestScore

def playComputer():
    bestScore = -100
    bestMove = 0

    for key in board.keys():
        if board[key] == " ":
            board[key] = "o"
            score = minimax(board , False) # minimax
            board[key] = " "
            if score > bestScore : 
                bestScore = score 
                bestMove = key

    board[bestMove] = "o"




#Function to play
def play(event):
    global turn,game_end
    if game_end:
        return
    
    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]
    if clicked == "n":
        clicked = 1
    else:
        clicked=int(clicked)

    if button["text"]==" ":
        if turn =="X":
            button["text"]="X"
            board[clicked]=turn
            if checkWin(turn):
                winLabel=Label(frame1,text=f"{turn} wins the game",bg="red",font=("Arial",26),width=16)
                winLabel.grid(row=0,column=0,columnspan=3)
                game_end=True

                """print(turn,"wins the game")
                print("Game Over")"""
            turn="o"

            upddateBoard()

            if mode =="singlePlayer":

                playComputer()
                if checkWin(turn):
                    winLabel=Label(frame1,text=f"{turn} wins the game",bg="red",font=("Arial",26),width=16)
                    winLabel.grid(row=0,column=0,columnspan=3)
                    game_end=True
                turn="X"

                upddateBoard()
            
        else:
            board[clicked]=turn
            upddateBoard()
            if checkWin(turn):
                winLabel=Label(frame1,text=f"{turn} wins the game",bg="green",font=("Arial",30),width=16)
                winLabel.grid(row=3,column=0,columnspan=3)
                game_end=True
            turn="X"

        if checkDraw():
            drawLabel=Label(frame1,text=f"Game Draw",bg="violet",font=("Arial",30),width=16)
            drawLabel.grid(row=3,column=0,columnspan=3)

# ------ UI --------

# Change Mode options 

singlePlayerButton = Button(optionFrame , text="SinglePlayer" , width=13 , height=1 , font=("Arial" , 15) , bg="lightgrey" , relief=RAISED , borderwidth=5 , command=changeTosinglePlayer)
singlePlayerButton.grid(row=0 , column=0 , columnspan=1 , sticky=NW)

multiPlayerButton = Button(optionFrame , text="Multiplayer" , width=13 , height=1 , font=("Arial" , 15) , bg="lightgrey" , relief=RAISED , borderwidth=5 , command=changeToMultiplayer )
multiPlayerButton.grid(row=0 , column=1 , columnspan=1 , sticky=NW)
    
    


#Tic Tac Toe Board


#First row
button1=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="yellow",relief=RAISED,borderwidth=5)
button1.grid(row=0,column=0)
button1.bind("<Button-1>" , play)

button2=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="yellow",relief=RAISED,borderwidth=5)
button2.grid(row=0,column=1)
button2.bind("<Button-1>" , play)

button3=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="yellow",relief=RAISED,borderwidth=5)
button3.grid(row=0,column=2)
button3.bind("<Button-1>" , play)

#Second row

button4=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="yellow",relief=RAISED,borderwidth=5)
button4.grid(row=1,column=0)
button4.bind("<Button-1>" , play)

button5=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="yellow",relief=RAISED,borderwidth=5)
button5.grid(row=1,column=1)
button5.bind("<Button-1>" , play)

button6=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="yellow",relief=RAISED,borderwidth=5)
button6.grid(row=1,column=2)
button6.bind("<Button-1>" , play)

#Third row

button7=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="yellow",relief=RAISED,borderwidth=5)
button7.grid(row=2,column=0)
button7.bind("<Button-1>" , play)

button8=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="yellow",relief=RAISED,borderwidth=5)
button8.grid(row=2,column=1)
button8.bind("<Button-1>" , play)

button9=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="yellow",relief=RAISED,borderwidth=5)
button9.grid(row=2,column=2)
button9.bind("<Button-1>" , play)

restartButton=Button(frame2,text="Restart Game",width=19,height=1,font=("Arial",30),bg="Green",relief=RAISED,borderwidth=5,command=restartGame)
restartButton.grid(row=4,column=0,columnspan=3)

buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9]

root.mainloop()