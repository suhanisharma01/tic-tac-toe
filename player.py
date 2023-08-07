board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
winner = None
gamerunning = True


def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

print_board(board)  

def boardfull(board):
    global gamerunning
    if '-' not in board:
        gamerunning = False
        return True
        
           
def horizontalwinner(board):
    global winner, gamerunning
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        gamerunning = False
        return True
    elif board[3] == board[4] == board[5] and board[4] != '-':
        winner = board[3] 
        gamerunning = False 
        return True
    elif board[6] == board[7] == board[8] and board[7] != '-':
        winner = board[6]
        gamerunning = False
        return True
       
def verticalwinner(board):
    global winner, gamerunning
    if board[0] == board[3] == board[6] and board[3] != '-':
        winner = board[0]
        gamerunning = False
        return True
    elif board[1] == board[4] == board[7] and board[4] != '-':
        winner = board[4]  
        gamerunning = False
        return True
    elif board[2] == board[5] == board[8] and board[8] != '-':
        winner = board[8]
        gamerunning = False
        return True

def diagonalwinner(board):
    global winner, gamerunning
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        gamerunning = False
        return True
    elif board[2] == board[4] == board[6] and board[6] != '-':
        winner = board[6]
        gamerunning = False  
        return True
          
def main():
    print('Player 1 is X and player 2 is O')

    while gamerunning:
        player1 = int(input("player 1 enter the box number to place your X from 1 to 9: ")) 
        if player1 >= 1 and player1 <= 9 and board[player1 - 1] == '-':
            board[player1 - 1] ='X'
        else:
            player1 = int(input("Oops, wrong input! player 1 please enter the box number to place your X from 1 to 9: "))  
            board[player1 - 1] = 'X'
        
        print_board(board) 
        boardfull(board)
        horizontalwinner(board)
        verticalwinner(board)
        diagonalwinner(board)     

        if gamerunning == False:
            break

        player2 = int(input("player 2 enter the box number to place your O from 1 to 9: ")) 
        if player2 >= 1 and player2 <= 9 and board[player2 - 1] == '-':
            board[player2 - 1] = 'O'
        else:
            player2 = int(input("Oops, wrong input! player 2 please enter the box number to place your O from 1 to 9: "))  
            board[player2 - 1] = 'O'

        print_board(board) 
        boardfull(board)
        horizontalwinner(board)
        verticalwinner(board)
        diagonalwinner(board)    
    
    if boardfull(board) == True:
        print('Its a tie')
    elif horizontalwinner(board) == True or verticalwinner(board) == True or diagonalwinner(board) == True:
        if winner == 'X':
            print('Player 1 won!')
        elif winner == 'O':
            print('Player 2 won!')       
                
main()           

            




