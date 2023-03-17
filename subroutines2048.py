import random
import math
import tkinter as tk


# run when start game button pressed
def runGame(root):
    global board
    global boardGUI
    
    boardWindow = tk.Toplevel(root)
    boardWindow.title('2048')
    
    SIZE =4
    
    board = createBoardMemory(SIZE)
    
    boardGUI = createBoardGUI(board,boardWindow,SIZE)
    
    board , boardGUI = addBlockToBoard(board,boardGUI)


# creates 2d list with all squares in board and numbers at each point as str
def createBoardMemory(size): 
    board = [['' for j in range(size)]for i in range(size)]
    return board


# creates GUI for the board and returns a 2d list with each label as an element
def createBoardGUI(board,window,SIZE):
    boardGUI = []
    
    for rowIndex , row in enumerate(board): # loop through rows
        boardGUI.append([])
        for columnIndex , column in enumerate(row): # loop through columns
            # create label for each position in board
            label = tk.Label(window, text='', height=10, width=30, borderwidth=2, relief="groove")
            label.grid(row=rowIndex,column=columnIndex) # adds label to screen
            boardGUI[rowIndex].append(label) # adds label to correct place in 2d list of labels
            
    # create buttons to move numbers
    up = tk.Button(window, text='Up', height=8, width=25, borderwidth=2, relief="groove", command=lambda:moveBoard('up'))
    up.grid(row=1,column=SIZE+1)
    
    down = tk.Button(window, text='Down', height=8, width=25, borderwidth=2, relief="groove", command=lambda:moveBoard('down'))
    down.grid(row=2,column=SIZE+1)
    
    right = tk.Button(window, text='Right', height=8, width=25, borderwidth=2, relief="groove", command=lambda:moveBoard('right'))
    right.grid(row=2,column=SIZE+2)
    
    left = tk.Button(window, text='Left', height=8, width=25, borderwidth=2, relief="groove", command=lambda:moveBoard('left'))
    left.grid(row=2,column=SIZE)

    return boardGUI


# adds a block to the board in a random position
def addBlockToBoard(board,gui):
    allowed = False
    while not allowed: # check that square isn't occupied
        newRow = random.randint(0,3)
        newCol = random.randint(0,3)
        if board[newRow][newCol] == '':
            allowed = True
    board[newRow][newCol] = '2'
    gui[newRow][newCol].config(text='2')
    changeColour(gui[newRow][newCol],2)
    
    
    return board , gui


# move all numbers on board in certain direction
def moveBoard(direction):
    global board
    global boardGUI
    
    if direction == 'up':
        allowed = False # is up an allowed move
        for rowIndex , row in enumerate(board): # loop theough rows
            if rowIndex != 0: # exclude the top row (can't go up form the top)
                for columnIndex , col in enumerate(row): # loop through each value in each row
                    if col != '' and board[rowIndex-1][columnIndex] == '': # see if there is a square with a value and no vlaue above it
                        allowed = True # the move is allowed
                
        swapped = True
        while swapped: # repeat process until there are no swaps
            swapped = False # no swaps so far in loop
            for rowIndex , row in enumerate(board):
                if rowIndex != 0: # make sure not already at top
                    for columnIndex , col in enumerate(row):
                        if board[rowIndex][columnIndex] != '': # check if current square isn't 0
                            if board[rowIndex-1][columnIndex] == '': # check if above square isn't 0
                                board[rowIndex-1][columnIndex] = board[rowIndex][columnIndex] # set above square to below square
                                board[rowIndex][columnIndex] = '' # reset current square to 0
                                swapped = True # show there was a swap
                            elif board[rowIndex-1][columnIndex] == board[rowIndex][columnIndex]: # if square above is same as current square
                                current = int(board[rowIndex][columnIndex]) # set values of squares to integers
                                above = int(board[rowIndex-1][columnIndex])
                                board[rowIndex-1][columnIndex] = str(current + above) # set square above to string of lower one added
                                board[rowIndex][columnIndex] = '' # reset current square to 0
                                swapped = True # show there was a swap
                                
    elif direction == 'down':
        allowed = False
        for rowIndex , row in enumerate(board):
            if rowIndex != len(row)-1:
                for columnIndex , col in enumerate(row):
                    if col != '' and board[rowIndex+1][columnIndex] == '':
                        allowed = True
                    
        swapped = True
        while swapped:
            swapped = False
            for rowIndex , row in enumerate(board):
                if rowIndex != len(row)-1:
                    for columnIndex , col in enumerate(row):
                        if board[rowIndex][columnIndex] != '':
                            if board[rowIndex+1][columnIndex] == '':
                                board[rowIndex+1][columnIndex] = board[rowIndex][columnIndex]
                                board[rowIndex][columnIndex] = ''
                                swapped = True
                            elif board[rowIndex+1][columnIndex] == board[rowIndex][columnIndex]:
                                current = int(board[rowIndex][columnIndex])
                                above = int(board[rowIndex+1][columnIndex])
                                board[rowIndex+1][columnIndex] = str(current + above)
                                board[rowIndex][columnIndex] = ''
                                swapped = True
                                
    elif direction == 'right':
        allowed = False
        for rowIndex , row in enumerate(board):
            for columnIndex , col in enumerate(row):
                if columnIndex != len(row)-1:
                    if col != '' and board[rowIndex][columnIndex-1] == '':
                        allowed = True
                
        swapped = True
        while swapped:
            swapped = False
            for rowIndex , row in enumerate(board):
                for columnIndex , col in enumerate(row):
                    if columnIndex != len(row)-1:
                        if board[rowIndex][columnIndex] != '':
                            if board[rowIndex][columnIndex+1] == '':
                                board[rowIndex][columnIndex+1] = board[rowIndex][columnIndex]
                                board[rowIndex][columnIndex] = ''
                                swapped = True
                            elif board[rowIndex][columnIndex+1] == board[rowIndex][columnIndex]:
                                current = int(board[rowIndex][columnIndex])
                                above = int(board[rowIndex][columnIndex+1])
                                board[rowIndex][columnIndex+1] = str(current + above)
                                board[rowIndex][columnIndex] = ''
                                swapped = True
                                
    elif direction == 'left':
        allowed = False
        for rowIndex , row in enumerate(board):
            for columnIndex , col in enumerate(row):
                if columnIndex != 0:
                    if col != '' and board[rowIndex][columnIndex-1] == '':
                        allowed = True
                
        swapped = True
        while swapped:
            swapped = False
            for rowIndex , row in enumerate(board):
                for columnIndex , col in enumerate(row):
                    if columnIndex != 0:
                        if board[rowIndex][columnIndex] != '':
                            if board[rowIndex][columnIndex-1] == '':
                                board[rowIndex][columnIndex-1] = board[rowIndex][columnIndex]
                                board[rowIndex][columnIndex] = ''
                                swapped = True
                            elif board[rowIndex][columnIndex-1] == board[rowIndex][columnIndex]:
                                current = int(board[rowIndex][columnIndex])
                                above = int(board[rowIndex][columnIndex-1])
                                board[rowIndex][columnIndex-1] = str(current + above)
                                board[rowIndex][columnIndex] = ''
                                swapped = True
                                
    updateGUI(board,boardGUI)
    
    if allowed:
        board, boardGUI = addBlockToBoard(board,boardGUI)
    
    
# update GUI with positions of board
def updateGUI(board,gui):
    for rowIndex , row in enumerate(board):
        for colIndex , col in enumerate(row):
            gui[rowIndex][colIndex].config(text=col)
            if col != '':
                changeColour(gui[rowIndex][colIndex],int(col))
            else:
                gui[rowIndex][colIndex].config(bg='#f0f0f0')
   
   
# set the colour of the label based on the number it displayss
def changeColour(label,num):
    colours = ['#ffffff','#ff9d5c','#ff781f','#ff6600','#ff0000', '#cc0000','#990000',
               '#660000','#4d0000','#330000','#190000','#45b6fe', '#3792cb','#296d98',
               '#1c4966','#0e2433'] # colours for values up to 65536
    multiplier = int(math.log2(num)) # find integer for log2 of value in square
    multiplier -= 1 # align the multiplier with indices of list
    label.config(bg=colours[multiplier]) # set the colour of the label to colour corresponding to mulitiplier