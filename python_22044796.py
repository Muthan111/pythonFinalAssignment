import random

#A function to print the board
def Print_board(list1):
    print()
    print("       |     |")
    print("    {}  |  {}  |  {}".format(list1[0], list1[1], list1[2]))
    print('  _____|_____|_____')
    print("       |     |")
    print("    {}  |  {}  |  {}".format(list1[3], list1[4], list1[5]))
    print('  _____|_____|_____')
    print("       |     |")
    print("    {}  |  {}  |  {}".format(list1[6], list1[7], list1[8]))
    print("       |     |")
    print()

# Important variable defined which will be used in the program
Computer_piece = 0
Human = "H"
i = 1

Row_Column = ["1,1","1,2","1,3","2,1","2,2","2,3","3,1","3,2","3,3"]
# Rules to follow when playing the game
Position =[1,2,3,4,5,6,7,8,9] # This shows the positions available for selection
Print_board(Position)
print("""Each number represents a tile 
Press the respective tiles number
to select your intended tile""")
print()    

#A function to record the user moves
Board_filled = [" "," "," "," "," "," "," "," "," "]
def User_move(Tile, User_option ):
    Board_filled[Tile - 1] = User_option
    Position.remove(Tile)
    Print_board(Board_filled)

#A function to record the computer moves
def Comp_move(Tiles, Computer_piece):
    Board_filled[Tiles  - 1] = Computer_piece
    Position.remove(Tiles)
    Print_board(Board_filled)

# A function to update the log file
def log_file(write1): 
    log_file = open("logfile_22044796.txt","a") 
    log_file.write(write1)
    log_file.close()

#A function which fills up the log file
J = 1
Computer = "C"
def fill_log_file(J,computer,Option,n):
    entry = str(J) +" "+ computer +" "+ Row_Column[n]+" " + Option + "\n"
    log_file(entry)
    J += 1

# A  function to fill the board with the computers moves
def fill_board(a,Computer_piece):
    Board_filled[a] = Computer_piece
    Print_board(Board_filled)
    Position.remove(a + 1)

#Functions to check the board
z = 0
N = 9    
count = 0
count1 = []
count2 = []
draw = 0
def checking(N,count, count1,count2, J, draw):
#This half of the code checks if two adjacent (Horizontal, vertical or diagonal) positions have been marked by the computer and puts its piece in the third tile.
    if Board_filled[0] == Board_filled[1] == Computer_piece and Board_filled[2] == " " and len(count1) < 2: 
        fill_board(2, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,2)
        N -= 1
        count += 1
    elif Board_filled[1] == Board_filled[2] == Computer_piece and Board_filled[0] == " " and len(count1) < 2: 
        fill_board(0, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,0)
        N -= 1
        count += 1
    elif Board_filled[0] == Board_filled[2] == Computer_piece and Board_filled[1] == " " and len(count1) < 2: 
        fill_board(1, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,1)
        N -= 1
        count += 1
    elif Board_filled[3] == Board_filled[4] == Computer_piece and Board_filled[5] == " "and len(count1) < 2: 
        fill_board(5, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,5)
        N -= 1
        count += 1
    elif Board_filled[5] == Board_filled[4] == Computer_piece and Board_filled[3] == " " and len(count1) < 2: 
        fill_board(3, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,3)
        N -= 1
        count += 1
    elif Board_filled[5] == Board_filled[3] == Computer_piece and Board_filled[4] == " " and len(count1) < 2: 
        fill_board(4, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,4)
        N -= 1
        count += 1
    elif Board_filled[6] == Board_filled[7] == Computer_piece and Board_filled[8] == " " and len(count1) < 2: 
        fill_board(8, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,8)
        N -= 1
        count += 1
    elif Board_filled[6] == Board_filled[8] == Computer_piece and Board_filled[7] == " " and len(count1) < 2: 
        fill_board(7, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,7)
        N -= 1
        count += 1
    elif Board_filled[8] == Board_filled[7] == Computer_piece and Board_filled[6] == " " and len(count1) < 2: 
        fill_board(6, Computer_piece)
        fill_log_file(J,Computer,Computer_piece,6)
        N -= 1
        count += 1
    elif Board_filled[0] == Board_filled[3] == Computer_piece and Board_filled[6] == " " and len(count1) < 2: 
        fill_board(6, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,6)
        N -= 1
        count += 1
    elif Board_filled[6] == Board_filled[3] == Computer_piece and Board_filled[0] == " " and len(count1) < 2: 
        fill_board(0, v)
        fill_log_file(J, Computer,Computer_piece,0)
        N -= 1
        count += 1
    elif Board_filled[0] == Board_filled[6] == Computer_piece and Board_filled[3] == " " and len(count1) < 2: 
        fill_board(3, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,3)
        N -= 1
        count += 1
    elif Board_filled[1] == Board_filled[4]== Computer_piece and Board_filled[7] == " " and len(count1) < 2: 
        fill_board(7, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,7)
        N -= 1
        count += 1
        print(N)
    elif Board_filled[1] == Board_filled[7]== Computer_piece and Board_filled[4] == " " and len(count1) < 2: 
        fill_board(4, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,4)
        N -= 1
        count += 1
    elif Board_filled[4] == Board_filled[7]== Computer_piece and Board_filled[1] == " " and len(count1) < 2: 
        fill_board(1, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,1)
        N -= 1
        count += 1
    elif Board_filled[2] == Board_filled[5]== Computer_piece and Board_filled[8] == " " and len(count1) < 2: 
        fill_board(8, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,8)
        N -= 1
        count += 1
    elif Board_filled[2] == Board_filled[8]== Computer_piece and Board_filled[5] == " " and len(count1) < 2: 
        fill_board(5, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,5)
        count += 1
        N -= 1
    elif Board_filled[5] == Board_filled[8]== Computer_piece and Board_filled[2] == " " and len(count1) < 2: 
        fill_board(2,Computer_piece)
        fill_log_file(J, Computer,Computer_piece,2)
        count += 1
        N -= 1
    elif Board_filled[0] == Board_filled[4]== Computer_piece and Board_filled[8] == " " and len(count1) < 2: 
        fill_board(8, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,8)
        count += 1
        N -= 1
    elif Board_filled[0] == Board_filled[8]== Computer_piece and Board_filled[4] == " " and len(count1) < 2: 
        fill_board(4, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,4)
        count += 1
        N -= 1
    elif Board_filled[8] == Board_filled[4]== Computer_piece and Board_filled[0] == " " and len(count1) < 2: 
        fill_board(0, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,0)
        count += 1
        N -= 1
    elif Board_filled[2] == Board_filled[4]== Computer_piece and Board_filled[6] == " " and len(count1) < 2: 
        fill_board(6, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,6)
        count += 1
        N -= 1
    elif Board_filled[2] == Board_filled[6]== Computer_piece and Board_filled[4] == " " and len(count1) < 2: 
        fill_board(4, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,4)
        count += 1
        N -= 1
    elif Board_filled[6] == Board_filled[4]== Computer_piece and Board_filled[2] == " " and len(count1) < 2: 
        fill_board(2, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,2)
        count += 1
        N -= 1

#This half of the code checks if two adjacent (Horizontal, vertical or diagonal) positions have been marked by the user and the computer puts its piece in the third tile.        
    elif Board_filled[0] == Board_filled[1] == User_option and Board_filled[2] == " " and len(count1) < 2: 
        fill_board(2, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,2)
        N -= 1
        count += 1
    elif Board_filled[1] == Board_filled[2] == User_option and Board_filled[0] == " " and len(count1) < 2: 
        fill_board(0, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,0)
        N -= 1
        count += 1
        print(N)
    elif Board_filled[0] == Board_filled[2] == User_option and Board_filled[1] == " " and len(count1) < 2: 
        fill_board(1, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,1)
        N -= 1
        count += 1
    elif Board_filled[3] == Board_filled[4] == User_option and Board_filled[5] == " "and len(count1) < 2: 
        fill_board(5, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,5)
        N -= 1
        count += 1
    elif Board_filled[5] == Board_filled[4] == User_option and Board_filled[3] == " " and len(count1) < 2: 
        fill_board(3, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,3)
        N -= 1
        count += 1
    elif Board_filled[5] == Board_filled[3] == User_option and Board_filled[4] == " " and len(count1) < 2: 
        fill_board(4, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,4)
        N -= 1
        count += 1
    elif Board_filled[6] == Board_filled[7] == User_option and Board_filled[8] == " " and len(count1) < 2: 
        fill_board(8, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,8)
        N -= 1
        count += 1
    elif Board_filled[6] == Board_filled[8] == User_option and Board_filled[7] == " " and len(count1) < 2: 
        fill_board(7, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,7)
        N -= 1
        count += 1
    elif Board_filled[8] == Board_filled[7] == User_option and Board_filled[6] == " " and len(count1) < 2: 
        fill_board(6, Computer_piece)
        fill_log_file(J,Computer,Computer_piece,6)
        N -= 1
        count += 1
    elif Board_filled[0] == Board_filled[3] == User_option and Board_filled[6] == " " and len(count1) < 2: 
        fill_board(6, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,6)
        N -= 1
        count += 1
    elif Board_filled[6] == Board_filled[3] == User_option and Board_filled[0] == " " and len(count1) < 2: 
        fill_board(0, v)
        fill_log_file(J, Computer,Computer_piece,0)
        N -= 1
        count += 1
    elif Board_filled[0] == Board_filled[6] == User_option and Board_filled[3] == " " and len(count1) < 2: 
        fill_board(3, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,3)
        N -= 1
        count += 1
    elif Board_filled[1] == Board_filled[4]== User_option and Board_filled[7] == " " and len(count1) < 2: 
        fill_board(7, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,7)
        N -= 1
        count += 1
    elif Board_filled[1] == Board_filled[7]== User_option and Board_filled[4] == " " and len(count1) < 2: 
        fill_board(4, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,4)
        N -= 1
        count += 1
    elif Board_filled[4] == Board_filled[7]== User_option and Board_filled[1] == " " and len(count1) < 2: 
        fill_board(1, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,1)
        N -= 1
        count += 1
    elif Board_filled[2] == Board_filled[5]== User_option and Board_filled[8] == " " and len(count1) < 2: 
        fill_board(8, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,8)
        N -= 1
        count += 1
    elif Board_filled[2] == Board_filled[8]== User_option and Board_filled[5] == " " and len(count1) < 2: 
        fill_board(5, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,5)
        count += 1
        N -= 1
    elif Board_filled[5] == Board_filled[8]== User_option and Board_filled[2] == " " and len(count1) < 2: 
        fill_board(2,Computer_piece)
        fill_log_file(J, Computer,Computer_piece,2)
        count += 1
        N -= 1
    elif Board_filled[0] == Board_filled[4]== User_option and Board_filled[8] == " " and len(count1) < 2: 
        fill_board(8, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,8)
        count += 1
        N -= 1
    elif Board_filled[0] == Board_filled[8]== User_option and Board_filled[4] == " " and len(count1) < 2: 
        fill_board(4, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,4)
        count += 1
        N -= 1
    elif Board_filled[8] == Board_filled[4]== User_option and Board_filled[0] == " " and len(count1) < 2: 
        fill_board(0, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,0)
        count += 1
        N -= 1
    elif Board_filled[2] == Board_filled[4]== User_option and Board_filled[6] == " " and len(count1) < 2: 
        fill_board(6, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,6)
        count += 1
        N -= 1
    elif Board_filled[2] == Board_filled[6]== User_option and Board_filled[4] == " " and len(count1) < 2: 
        fill_board(4, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,4)
        count += 1
        N -= 1
    elif Board_filled[6] == Board_filled[4]== User_option and Board_filled[2] == " " and len(count1) < 2: 
        fill_board(2, Computer_piece)
        fill_log_file(J, Computer,Computer_piece,2)
        count += 1
        N -= 1
#If the above conditions are not met, then this code below will run        
    else:   
        if len(Position) == 0:
            draw ="Game over"
            return draw
            
        elif len(Position) != 0 :
            comp_move = Position[random.randint(0,N)]
            Comp_move(comp_move, Computer_piece)
            entry = str(J) +" "+Computer+" "+ Row_Column[random.randint(0,N)]+" " + Computer_piece + "\n"
            log_file(entry)
            J += 1
            N -= 1    
            count += 1
            count2.append(count)
            
#Function to check if computer or player won
p = "Player"
c = "Computer"            
def check_win(User_option,Computer_piece,c,p,i2):
    if Board_filled[0] == Board_filled[1] == User_option and Board_filled[2] == User_option:
        i2 = "{} win".format(p)
        return i2
    elif Board_filled[3] == Board_filled[4] == User_option and Board_filled[5] == User_option:
        i2 = "{} win".format(p)
        return i2
    elif Board_filled[6] == Board_filled[7] == User_option and Board_filled[8] == User_option:
        i2 = "{} win".format(p)
        return i2
    elif Board_filled[0] == Board_filled[3] == User_option and Board_filled[6] == User_option:
        i2 = "{} win".format(p)
        return i2
    elif Board_filled[1] == Board_filled[4] == User_option and Board_filled[7] == User_option:
        i2 = "{} win".format(p)
        return i2
    elif Board_filled[2] == Board_filled[5] == User_option and Board_filled[8] == User_option:
        i2 = "{} win".format(p)
        return i2
    elif Board_filled[0] == Board_filled[4] == User_option and Board_filled[8] == User_option:
        i2 = "{} win".format(p)
        return i2
    elif Board_filled[2] == Board_filled[4] == User_option and Board_filled[6] == User_option:
        i2 = "{} win".format(p)
        return i2
    # Computer    
    elif Board_filled[0] == Board_filled[1] == Computer_piece and Board_filled[2] == Computer_piece:
        i2 = "{} win".format(c)
        return i2
    elif Board_filled[3] == Board_filled[4] == Computer_piece and Board_filled[5] == Computer_piece:
        i2 = "{} win".format(c)
        
        return i2
    elif Board_filled[6] == Board_filled[7] == Computer_piece and Board_filled[8] == Computer_piece:
        i2 = "{} win".format(c)
        return i2
    elif Board_filled[0] == Board_filled[3] == Computer_piece and Board_filled[6] == Computer_piece:
        i2 = "{} win".format(c)
        return i2
    elif Board_filled[1] == Board_filled[4] == Computer_piece and Board_filled[7] == Computer_piece:
        i2 = "{} win".format(c)
        return i2
    elif Board_filled[2] == Board_filled[5] == Computer_piece and Board_filled[8] == Computer_piece:
        i2 = "{} win".format(c)
        return i2
    elif Board_filled[0] == Board_filled[4] == Computer_piece and Board_filled[8] == Computer_piece:
        i2 = "{} win".format(c)
        return i2
    elif Board_filled[2] == Board_filled[4] == Computer_piece and Board_filled[6] == Computer_piece:
        i2 = "{} win".format(c)
        return i2
    

# The games function
Game = "Y"
#A loop to keep the game going
while Game == "Y":
    Board_filled = [" "," "," "," "," "," "," "," "," "]
    Position =[1,2,3,4,5,6,7,8,9]
    N = 9
    #User can select either X or O
    User_option = input("Choose X or O: ")      
    if User_option == "X" or User_option == "x":
        
        #Computer piece is automatically set after User_option is selected
        Computer_piece = "O"                   
        
        #Users first move 
        user_move =int(input("Enter the number of the tile you wish to select: "))

        #This code validates the data the user inputs
        if Board_filled[user_move - 1] == " ":
                User_move(user_move, User_option)
                N -= 1
                entry2 = str(J)+" "+Human+" " + Row_Column[user_move - 1]+" " + User_option +"\n"
                log_file(entry2)
                J += 1
                
                
        # This runs the data is the correct type but is wrong
        else:
            print("error")
            user_move = int(input("Enter the number of the tile you wish to select: "))
            User_move(user_move, User_option)
            N = N - 1
            entry2 = str(J)+" "+Human+" " + Row_Column[user_move - 1]+" " + User_option +"\n"
            log_file(entry2)
            J += 1

        #Computers first move
        comp_move1 = Position[random.randint(0,N)]
        Comp_move(comp_move1, Computer_piece)
        entry2 = str(J) +" "+Computer+" "+ Row_Column[comp_move1 - 1 ]+" " + Computer_piece + "\n"
        log_file(entry2)
        N -= 1
        J += 1
        
        
        # Loop to keep the game Going
        for i in range(4):
            
            #users turn
            user_move1 = int(input("Enter the number of the tile you wish to select: "))
            if Board_filled[user_move1 - 1] == " ":
                User_move(user_move1, User_option)
                N -= 1
                entry2 = str(J) +" "+Human+" "+ Row_Column[user_move1 - 1]+" " + User_option + "\n"
                log_file(entry2)
                J += 1
            elif len(Position) == 0:
                print("ITS A TIE")
                
            else:
                print("error")
                user_move1 = int(input("Enter the number of the tile you wish to select: "))
                User_move(user_move1, User_option)
                N = N - 1
                entry2 = str(J) +" "+Human+" "+ Row_Column[user_move1 - 1]+" " + User_option + "\n"
                log_file(entry2)
                J += 1
                
            #Computers turn
            game_draw = checking(N,count, count1,count2, J, draw)
            winner = check_win(User_option,Computer_piece,c,p,z)
            N -= 1
            
            if winner == "Computer win":
                print("Computer wins")
                break
            if winner == "Player win":
                print("Player wins")
                break    
            if game_draw == "Game over":
                break
        Game = str(input("Play again?: "))
        
            
            
            
            
            
           
    #Code to run if user selects "O"        
    elif User_option == "O":
        Computer_piece = "X"
        comp_move = Position[random.randint(0,N)]
        Comp_move(comp_move, Computer_piece)
        entry2 = str(J) +" "+Computer+" "+ Row_Column[comp_move - 1 ]+" " + Computer_piece + "\n"
        log_file(entry2)
        N -= 1
        J += 1
        
        # user chooses a position on the grid
        
        user_move1 = int(input("Enter the number of the tile you wish to select: "))
        User_move(user_move1, User_option)
        entry1 = str(J)+" "+Human+" " + Row_Column[user_move1 - 1]+" " + User_option +"\n"
        log_file(entry1)
        N -= 1
        J += 1
        for i in range(4):
            game_draw = checking(N,count, count1,count2, J, draw)
            winner = check_win(User_option,Computer_piece,c,p,z)
            N -= 1

            if winner == "Computer win":
                print("Computer wins")
                break 
            
            user_move1 = int(input("Enter the number of the tile you wish to select: "))
            if Board_filled[user_move1 - 1] == " ":
                User_move(user_move1, User_option)
                N -= 1
                entry2 = str(J) +" "+Human+" "+ Row_Column[user_move1 - 1]+" " + User_option + "\n"
                log_file(entry2)
                J += 1
                
            elif len(Position) == 0:
                print("ITS A TIE")
                
            else:
                print("error")
                user_move1 = int(input("Enter the number of the tile you wish to select: "))
                User_move(user_move1, User_option)
                N = N - 1
                entry2 = str(J) +" "+Human+" "+ Row_Column[user_move1 - 1]+" " + User_option + "\n"
                log_file(entry2)
                J += 1

           
            if winner == "Player win":
                print("Player wins")
                break    
            if game_draw == "Game over":
                break
        Game = str(input("Play again?: "))
            
        
    #Code to run if user input is neither X nor O        
    else:
        print("Invalid input. You must enter either X or O")
        Game = str(input("Enter Y to start the game: "))
        print()        
