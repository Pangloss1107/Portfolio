import random
#class DIrector: 
#Functions: __init__ (Start the score with 300 points. Is_playing start with a boolean value (True). Here start the total_score = 0)
#           start_game(This function will call all the functions if is_playing == True)
#           show_card(This function will call the Cards class and will show a random card between 1 to 13)
#           get_input(This function will ask if the next card is higher or lower and it recieves an user's input (H or L))
#           show_new_card(This function will call the Cards class and will show a random card between 1 to 13)
#           calculate(In this function we will calculate the value if the user's choice is correct and if the choice is correct we will add 100 points. If the answer is wrong we rest 75 points)
#           show_score(This function will show the total score adding the points recieved in calculate function with the points in start score)
#           try_again(ASk the users if they want to play again if answer is Y the game will run again. If answer is N print in the screen "Game Over" )


#class Croupier: 
#Functions
#           __init__(Inicia el conteo desde 0)
#           give_number(This function will give a random number between 1,13) 

def numero():
    numero = random.randint(1,14)
    return numero


print(f"Pablo: {numero()}")
print(f"Renzo: {numero()}")
print(f"Valentina: {numero()}")
