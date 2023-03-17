    #Your program must also meet the following requirements.

    #The program must have a comment with assignment and author names.
    #The program must have at least one if/then block.
    #The program must have at least one while loop.
    #The program must have more than one function.
    #The program must have a function called main.

    # Tic-Tac-Toe activity - Pablo Santos
     

print("Tic-Tac-Toe - Pablo Santos")
print()
current_player = "X"
board = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]

def main():
    
    while not (winner(board) or draw(board)):
        #Show the board
        showboard(board)
        #Ask player to choose a number
        playermove(board)
        change_player()
    showboard(board)
    print()
    print("Game Over! Thanks for playing")

#function that will print the board
def showboard(board):
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

#Take the player move
def playermove(board): 
    move = int(input("Enter a number (1-9): "))
    if move >= 1 and move <=9:
        board[move - 1] = current_player
        print()
    else: 
        print("You can not do that move")
        print()

# Function to obtain a winner 
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
#Function if there is a draw 
def draw(board):
    for x in range(9):
        if board[x] != "X" and board[x] != "O":
            return False   
    return True   
    
        

#This function will change the player (X or O)
def change_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  else: 
      current_player = "X"

if __name__ == "__main__":
    main()