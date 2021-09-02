
board = {
    'R1': ' ', 'R2': ' ', 'R3': ' ',
    'R4': ' ', 'R5': ' ', 'R6': ' ',
    'R7': ' ', 'R8': ' ', 'R9': ' ',
}


def check(pl1, pl2):
    if board['R1'] == board['R2'] == board['R3'] == 'X' or board['R4'] == board['R5'] == board['R6'] == 'X' or board['R7'] == board['R8'] == board['R9'] == 'X':
        print(pl1+' Won!')
        return 1
    elif board['R1'] == board['R4'] == board['R7'] == 'X' or board['R2'] == board['R5'] == board['R8'] == 'X' or board['R3'] == board['R6'] == board['R9'] == 'X':
        print(pl1+' Won!')
        return 1
    elif board['R1'] == board['R5'] == board['R9'] == 'X' or board['R3'] == board['R5'] == board['R7'] == 'X':
        print(pl1+' Won!')
        return 1
    elif board['R1'] == board['R2'] == board['R3'] == 'O' or board['R4'] == board['R5'] == board['R6'] == 'O' or board['R7'] == board['R8'] == board['R9'] == 'O':
        print(pl2+' Won!')
        return 1
    elif board['R1'] == board['R4'] == board['R7'] == 'O' or board['R2'] == board['R5'] == board['R8'] == 'O' or board['R3'] == board['R6'] == board['R9'] == 'O':
        print(pl2+' Won!')
        return 1
    elif board['R1'] == board['R5'] == board['R9'] == 'O' or board['R3'] == board['R5'] == board['R7'] == 'O':
        print(pl2+' Won!')
        return 1


print('R1 | R2 | R3')
print('---+----+---')
print('R4 | R5 | R6')
print('---+----+---')
print('R7 | R8 | R9')
print('****************************')

player1 = str(input('Name of player one :'))
player2 = str(input('Name of player two :'))
player = player1
rounds = 1

while True:
    print(board['R1']+' | '+board['R2']+' | '+board['R3'])
    print('--+---+--')
    print(board['R4']+' | '+board['R5']+' | '+board['R6'])
    print('--+---+--')
    print(board['R7']+' | '+board['R8']+' | '+board['R9'])
    print('****************************')
    if check(player1, player2):
        break
    if rounds > 9:
        print("Game over!!!")
        print("Draw!!!")
        break

    print(rounds)
    while True:
        if player == player1:
            p1 = input('Player one :')
            if p1.upper() in board and board[p1.upper()] == ' ':
                board[p1.upper()] = 'X'
                player = player2
                break
            else:
                print('Invalid input! Try again')
        else:
            p2 = input('Player two :')
            if p2.upper() in board and board[p2.upper()] == ' ':
                board[p2.upper()] = 'O'
                player = player1
                break
            else:
                print('Invalid input! Try again')

    rounds += 1

    print('****************************')




