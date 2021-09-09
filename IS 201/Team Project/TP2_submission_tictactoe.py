# David Martinez, Jay Johnston, Sierra Honeycutt

# Defining the routine that takes turns
#     and processes the input positions
#     and updates the board and your datatypes.
# Adding file logging routine.
# Define your next steps.

# Known bugs to squash.
#  1. AI randomly not playing every round, why?
#  2. Would you like to go first? won't accept 'N' or 'n' now, why?
#  3. Add check for non X or O for player piece input
#  4. player_move other than 1-9, produces message but also does else statement.

import random                       # used in ai_choice() and computer_move()
file = open('tictactoe.txt', 'a')   # open file in append mode

class TicTacToe():
    def __init__(self):
        self.player_piece = ''      # Player piece selected/given
        self.computer_piece = ''    # AI piece selected/given
        self.b1 = ' '               # Board position 1
        self.b2 = ' '
        self.b3 = ' '
        self.b4 = ' '
        self.b5 = ' '
        self.b6 = ' '
        self.b7 = ' '
        self.b8 = ' '
        self.b9 = ' '               # Board position 9

    def display_board(self):
            print(f'         @-----------@      You are < ' + self.player_piece + ' >           @-----------@\n'
                  f'         | 7 | 8 | 9 |                              | ' + self.b7 + ' | ' + self.b8 + ' | ' + self.b9 + ' |\n'
                  f'  Board  |-----------|                         Your |-----------|\n'
                  f'         | 4 | 5 | 6 |                              | ' + self.b4 + ' | ' + self.b5 + ' | ' + self.b6 + ' |\n'
                  f' Choices |-----------|                        Board |-----------|\n'
                  f'         | 1 | 2 | 3 |                              | ' + self.b1 + ' | ' + self.b2 + ' | ' + self.b3 + ' |\n'
                  f'         @-----------@      A.I. is < ' + self.computer_piece + ' >           @-----------@\n')

    def player_decides(self):
        ''' Player decides to play first or not. If yes, then choose a piece. '''
        first = input('Would you like to go first? Y or N: ').upper()
        if first == 'Y':
            player_piece = input('What piece would you like? X or O: ').upper()
            if player_piece == 'X':
                self.player_piece = 'X'
                self.computer_piece = 'O'
                self.display_board()
                self.player_move()
            elif player_piece == 'O':
                self.player_piece = 'O'
                self.computer_piece = 'X'
                self.display_board()
                self.player_move()
            elif player_piece != 'X' or player_piece != 'O':
                self.player_decides()
        elif first != 'Y' or first != 'N':
            self.player_decides()
        elif first == 'N':
            self.computer_decides()
        else:
            self.computer_decides()

    def computer_decides(self):
        ''' AI randomly chooses if they want X or O. '''
        if random.randint(0, 1) == 0:
            self.computer_piece = 'X'
            self.player_piece = 'O'
            print(f'Okay, you\'ll be "{self.player_piece}" and I\'ll be "{self.computer_piece}"')
            self.computer_move()
        else:
            self.computer_piece = 'O'
            self.player_piece = 'X'
            print(f'Okay, you\'ll be "{self.player_piece}" and I\'ll be "{self.computer_piece}"')
            self.computer_move()

    def player_move(self):
        my_move = 0
        
        while True:
            ''' Catch wrong input '''
            try:
                my_move = int(input('Choose your move, 1-9: '))
            except ValueError:
                print('Only a number between 1 and 9, please. Try again.')
            
            ''' Is move choice viable choice? '''
            if my_move == 1 and self.b1 == ' ':
                self.b1 = self.player_piece
                file.write("Player chooses position 1.\n")
                ttt.display_board()
                self.win_or_tie_check()
                self.computer_move()
            elif my_move == 2 and self.b2 == ' ':
                self.b2 = self.player_piece
                file.write("Player chooses position 2.\n")
                ttt.display_board()
                self.win_or_tie_check()
                self.computer_move()
            elif my_move == 3 and self.b3 == ' ':
                self.b3 = self.player_piece
                file.write("Player chooses position 3.\n")
                ttt.display_board()
                self.win_or_tie_check()
                self.computer_move()
            elif my_move == 4 and self.b4 == ' ':
                self.b4 = self.player_piece
                file.write("Player chooses position 4.\n")
                ttt.display_board()
                self.win_or_tie_check()
                self.computer_move()
            elif my_move == 5 and self.b5 == ' ':
                self.b5 = self.player_piece
                file.write("Player chooses position 5.\n")
                ttt.display_board()
                self.win_or_tie_check()
                self.computer_move()
            elif my_move == 6 and self.b6 == ' ':
                self.b6 = self.player_piece
                file.write("Player chooses position 6.\n")
                ttt.display_board()
                self.win_or_tie_check()
                self.computer_move()
            elif my_move == 7 and self.b7 == ' ':
                self.b7 = self.player_piece
                file.write("Player chooses position 7.\n")
                ttt.display_board()
                self.win_or_tie_check()
                self.computer_move()
            elif my_move == 8 and self.b8 == ' ':
                self.b8 = self.player_piece
                file.write("Player chooses position 8.\n")
                ttt.display_board()
                self.win_or_tie_check()
                self.computer_move()
            elif my_move == 9 and self.b9 == ' ':
                self.b9 = self.player_piece
                file.write("Player chooses position 9.\n")
                ttt.display_board()
                self.win_or_tie_check()
                self.computer_move()
            else:
                print('That position is not empty, try again.')

    def ai_win_move(self):
        ai_move = 0
        ''' Check move sets for a winning move to place. '''
        if (self.b2 == self.computer_piece and self.b3 == self.computer_piece) or (self.b4 == self.computer_piece and self.b7 == self.computer_piece):
            ai_move = 1
        elif (self.b1 == self.computer_piece and self.b3 == self.computer_piece) or (self.b5 == self.computer_piece and self.b8 == self.computer_piece):
            ai_move = 2
        elif (self.b1 == self.computer_piece and self.b2 == self.computer_piece) or (self.b6 == self.computer_piece and self.b9 == self.computer_piece):
            ai_move = 3
        elif (self.b5 == self.computer_piece and self.b6 == self.computer_piece) or (self.b1 == self.computer_piece and self.b7 == self.computer_piece):
            ai_move = 4
        elif (self.b4 == self.computer_piece and self.b6 == self.computer_piece) or (self.b2 == self.computer_piece and self.b8 == self.computer_piece):
            ai_move = 5
        elif (self.b4 == self.computer_piece and self.b5 == self.computer_piece) or (self.b3 == self.computer_piece and self.b9 == self.computer_piece):
            ai_move = 6
        elif (self.b8 == self.computer_piece and self.b9 == self.computer_piece) or (self.b1 == self.computer_piece and self.b4 == self.computer_piece):
            ai_move = 7
        elif (self.b2 == self.computer_piece and self.b5 == self.computer_piece) or (self.b7 == self.computer_piece and self.b9 == self.computer_piece):
            ai_move = 8
        elif (self.b7 == self.computer_piece and self.b8 == self.computer_piece) or (self.b3 == self.computer_piece and self.b6 == self.computer_piece):
            ai_move = 9
        return ai_move

    def ai_block_move(self):
        ai_move = 0
        ''' Check move sets for a block move to place. '''
        if (self.b2 == self.player_piece and self.b3 == self.player_piece) or (self.b4 == self.player_piece and self.b7 == self.player_piece):
            ai_move = 1
        elif (self.b1 == self.player_piece and self.b3 == self.player_piece) or (self.b5 == self.player_piece and self.b8 == self.player_piece):
            ai_move = 2
        elif (self.b1 == self.player_piece and self.b2 == self.player_piece) or (self.b6 == self.player_piece and self.b9 == self.player_piece):
            ai_move = 3
        elif (self.b5 == self.player_piece and self.b6 == self.player_piece) or (self.b1 == self.player_piece and self.b7 == self.player_piece):
            ai_move = 4
        elif (self.b4 == self.player_piece and self.b6 == self.player_piece) or (self.b2 == self.player_piece and self.b8 == self.player_piece):
            ai_move = 5
        elif (self.b4 == self.player_piece and self.b5 == self.player_piece) or (self.b3 == self.player_piece and self.b9 == self.player_piece):
            ai_move = 6
        elif (self.b8 == self.player_piece and self.b9 == self.player_piece) or (self.b1 == self.player_piece and self.b4 == self.player_piece):
            ai_move = 7
        elif (self.b2 == self.player_piece and self.b5 == self.player_piece) or (self.b7 == self.player_piece and self.b9 == self.player_piece):
            ai_move = 8
        elif (self.b7 == self.player_piece and self.b8 == self.player_piece) or (self.b3 == self.player_piece and self.b6 == self.player_piece):
            ai_move = 9
        return ai_move

    def computer_move(self):
        ''' Dumb'ish AI picker '''
        ai_move = 0
        self.ai_block_move()
        self.ai_win_move()
        while ai_move == 0:
            if self.ai_block_move() == 0 and self.ai_win_move() == 0:
                ai_move = random.randrange(1,9)
            else:
                if self.ai_block_move() != 0:
                    ai_move = self.ai_block_move()
                if self.ai_win_move() != 0:
                    ai_move = self.ai_win_move()

            ''' Is move choice viable?. '''
            if ai_move == 1:
                if self.b1 == ' ':
                    self.b1 = self.computer_piece
                    ttt.display_board()
                    self.win_or_tie_check()
                    print('My move is position 1, now your move.')
                    file.write('AI chooses position 1.\n')
                    self.player_move()
                else:
                    self.computer_move()
            elif ai_move == 2:
                if self.b2 == ' ':
                    self.b2 = self.computer_piece
                    ttt.display_board()
                    self.win_or_tie_check()
                    print('My move is position 2, now your move.')
                    file.write('AI chooses position 2.\n')
                    self.player_move()
                else:
                    self.computer_move
            elif ai_move == 3:
                if self.b3 == ' ':
                    self.b3 = self.computer_piece
                    ttt.display_board()
                    self.win_or_tie_check()
                    print('My move is position 3, now your move.')
                    file.write('AI chooses position 3.\n')
                    self.player_move()
                else:
                    self.computer_move
            elif ai_move == 4:
                if self.b4 == ' ':
                    self.b4 = self.computer_piece
                    ttt.display_board()
                    self.win_or_tie_check()
                    print('My move is position 4, now your move.')
                    file.write('AI chooses position 4.\n')
                    self.player_move()
                else:
                    self.computer_move
            elif ai_move == 5:
                if self.b5 == ' ':
                    self.b5 = self.computer_piece
                    ttt.display_board()
                    self.win_or_tie_check()
                    print('My move is position 5, now your move.')
                    file.write('AI chooses position 5.\n')
                    self.player_move()
                else:
                    self.computer_move
            elif ai_move == 6:
                if self.b6 == ' ':
                    self.b6 = self.computer_piece
                    ttt.display_board()
                    self.win_or_tie_check()
                    print('My move is position 6, now your move.')
                    file.write('AI chooses position 6.\n')
                    self.player_move()
                else:
                    self.computer_move
            elif ai_move == 7:
                if self.b7 == ' ':
                    self.b7 = self.computer_piece
                    ttt.display_board()
                    self.win_or_tie_check()
                    print('My move is position 7, now your move.')
                    file.write('AI chooses position 7.\n')
                    self.player_move()
                else:
                    self.computer_move
            elif ai_move == 8:
                if self.b8 == ' ':
                    self.b8 = self.computer_piece
                    ttt.display_board()
                    self.win_or_tie_check()
                    print('My move is position 8, now your move.')
                    file.write('AI chooses position 8.\n')
                    self.player_move()
                else:
                    self.computer_move
            elif ai_move == 9:
                if self.b9 == ' ':
                    self.b9 = self.computer_piece
                    ttt.display_board()
                    self.win_or_tie_check()
                    print('My move is position 9, now your move.')
                    file.write('AI chooses position 9.\n')
                    self.player_move()
                else:
                    self.computer_move
            else:
                self.win_or_tie_check()

    def win_or_tie_check(self):
        if self.b1 == self.player_piece and self.b2 == self.player_piece and self.b3 == self.player_piece:
            print('Congratulations, you won!\n')
            file.write('Congratulations, you won!\n')
            file.close()
            exit()
        elif self.b4 == self.player_piece and self.b5 == self.player_piece and self.b6 == self.player_piece:
            print('Congratulations, you won!\n')
            file.write('Congratulations, you won!\n')
            file.close()
            exit()
        elif self.b7 == self.player_piece and self.b8 == self.player_piece and self.b9 == self.player_piece:
            print('Congratulations, you won!\n')
            file.write('Congratulations, you won!\n')
            file.close()
            exit()
        elif self.b7 == self.player_piece and self.b4 == self.player_piece and self.b1 == self.player_piece:
            print('Congratulations, you won!\n')
            file.write('Congratulations, you won!\n')
            file.close()
            exit()
        elif self.b8 == self.player_piece and self.b5 == self.player_piece and self.b2 == self.player_piece:
            print('Congratulations, you won!\n')
            file.write('Congratulations, you won!\n')
            file.close()
            exit()
        elif self.b9 == self.player_piece and self.b6 == self.player_piece and self.b3 == self.player_piece:
            print('Congratulations, you won!\n')
            file.write('Congratulations, you won!\n')
            file.close()
            exit()
        elif self.b7 == self.player_piece and self.b5 == self.player_piece and self.b3 == self.player_piece:
            print('Congratulations, you won!\n')
            file.write('Congratulations, you won!\n')
            file.close()
            exit()
        elif self.b9 == self.player_piece and self.b5 == self.player_piece and self.b1 == self.player_piece:
            print('Congratulations, you won!\n')
            file.write('Congratulations, you won!\n')
            file.close()
            exit()
        elif self.b1 == self.computer_piece and self.b2 == self.computer_piece and self.b3 == self.computer_piece:
            print('I Win! Computers RULE, this player drools!\n')
            file.write('I Win! Computers RULE, this player drools!\n')
            file.close()
            exit()
        elif self.b4 == self.computer_piece and self.b5 == self.computer_piece and self.b6 == self.computer_piece:
            print('I Win! Computers RULE, this player drools!\n')
            file.write('I Win! Computers RULE, this player drools!\n')
            file.close()
            exit()
        elif self.b7 == self.computer_piece and self.b8 == self.computer_piece and self.b9 == self.computer_piece:
            print('I Win! Computers RULE, this player drools!\n')
            file.write('I Win! Computers RULE, this player drools!\n')
            file.close()
            exit()
        elif self.b7 == self.computer_piece and self.b4 == self.computer_piece and self.b1 == self.computer_piece:
            print('I Win! Computers RULE, this player drools!\n')
            file.write('I Win! Computers RULE, this player drools!\n')
            file.close()
            exit()
        elif self.b8 == self.computer_piece and self.b5 == self.computer_piece and self.b2 == self.computer_piece:
            print('I Win! Computers RULE, this player drools!\n')
            file.write('I Win! Computers RULE, this player drools!\n')
            file.close()
            exit()
        elif self.b9 == self.computer_piece and self.b6 == self.computer_piece and self.b3 == self.computer_piece:
            print('I Win! Computers RULE, this player drools!\n')
            file.write('I Win! Computers RULE, this player drools!\n')
            exit()
        elif self.b7 == self.computer_piece and self.b5 == self.computer_piece and self.b3 == self.computer_piece:
            print('I Win! Computers RULE, this player drools!\n')
            file.write('I Win! Computers RULE, this player drools!\n')
            file.close()
            exit()
        elif self.b9 == self.computer_piece and self.b5 == self.computer_piece and self.b1 == self.computer_piece:
            print('I Win! Computers RULE, this player drools!\n')
            file.write('I Win! Computers RULE, this player drools!\n')
            file.close()
            exit()
        elif self.b1 != ' ' and self.b2 != ' ' and self.b3 != ' ' and self.b4 != ' ' and self.b5 != ' ' \
            and self.b6 != ' ' and self.b7 != ' ' and self.b8 != ' ' and self.b9 != ' ':
            print('This game was a tie!\n')
            file.write('This game was a tie!\n')
            file.close()
            exit()

ttt = TicTacToe()
ttt.player_decides()
