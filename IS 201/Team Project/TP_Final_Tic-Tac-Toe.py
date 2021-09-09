# David Martinez

# Known bugs to squash.
#  1. AI randomly not playing every round when player goes first, why?
#       << Fixed, rewrote computer_move(). >>
#  2. Would you like to go first? won't accept 'N' or 'n' now, why?
#       << Fixed, moved elif line up one level in statement. >>
#  3. Add check for non X or O for player piece input
#       << Created seperate player_first() routine >>
#  4. Player_move other than 1-9, produces message but also does else statement.
#       << Created while loop looking for ValueError >>
#  5. When AI goes first, it tanks after x-moves and exits with messages.
#       RecursionError: maximum recursion depth exceeded
#       << Fixed, rewrote code to use a dictionary for stored board keys/values. >>
#  6. AI not blocking/winning when it should. Missing two block moves from list.
#       << Maybe fixed, found comparisons were missing 3rd value, the empty ' ' >>
#       << Fixed inconsistencies in comparisons. >>
#  7. Rewrote win_or_tie_check() to use a list of winning combination to check.

import random                       # used in ai_choice() and computer_move()
file = open('tictactoe.txt', 'a')   # open file in append mode

class TicTacToe():
    def __init__(self):
        self.player_piece = ''      # Player piece selected/given
        self.computer_piece = ''    # AI piece selected/given
        self.board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ',            # board positions
                      6:' ', 7:' ', 8:' ', 9:' ', }
        self.winner_combos = [ [7, 4, 1], [8, 5, 2], [9, 6, 3],     # winning combinations
                                [7, 8, 9], [4, 5, 6], [1, 2, 3],
                                [7, 5, 3], [9, 5, 1], ]

    def display_board(self):
            print(f'         @-----------@      You are < ' + self.player_piece + ' >           @-----------@\n'
                  f'         | 7 | 8 | 9 |                              | ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9] + ' |\n'
                  f'  Board  |-----------|                         Your |-----------|\n'
                  f'         | 4 | 5 | 6 |                              | ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6] + ' |\n'
                  f' Choices |-----------|                        Board |-----------|\n'
                  f'         | 1 | 2 | 3 |                              | ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3] + ' |\n'
                  f'         @-----------@      A.I. is < ' + self.computer_piece + ' >           @-----------@\n')

    def player_decides(self):
        ''' Player decides to play first or not. If yes, then choose a piece. '''
        first = input('Would you like to go first? Y or N: ').upper() # store uppercase value
        if first == 'Y':                    # player wants to go first 
            self.player_first()
        elif first == 'N':                  # player doesn't want to go first
            self.computer_decides()
        else: # loop back if anything other than 'Y' or 'N'
            print("Please select 'Y' or 'N'.")
            self.player_decides()

    def player_first(self):
        player_piece = input('What piece would you like? X or O: ').upper() # store uppercase value
        if player_piece == 'X':         # player chooses 'X'
            self.player_piece = 'X'     
            self.computer_piece = 'O'   # AI assigned 'O'
            self.display_board()
            self.player_move()
        elif player_piece == 'O':       # player chooses 'O'
            self.player_piece = 'O'
            self.computer_piece = 'X'   # AI assigned 'X'
            self.display_board()
            self.player_move()
        else:
            print("Please select 'X' or 'O'.")
            self.player_first()

    def computer_decides(self):
        ''' AI randomly chooses if they want X or O. '''
        if random.randint(0, 1) == 0:
            self.computer_piece = 'X'
            self.player_piece = 'O'
            print(f'Okay, you\'ll be "{self.player_piece}" and I\'ll be "{self.computer_piece}."')
            self.computer_move()
        else:
            self.computer_piece = 'O'
            self.player_piece = 'X'
            print(f'Okay, you\'ll be "{self.player_piece}" and I\'ll be "{self.computer_piece}."')
            self.computer_move()

    def player_move(self):
        my_move = 0
        while True:                                 # error catching loop
            try:
                my_move = int(input('Choose your move, 1-9: '))
                if my_move < 1 or my_move > 9:      # catch wrong integer input
                    raise ValueError
                break
            except ValueError:                      # catch letter input
                print('Only a number between 1 and 9, please. Try again.')
                continue
        if self.board[my_move] == ' ':              # play my valid move
            self.board[my_move] = self.player_piece
            ttt.display_board()
            print(f'Player chooses position {my_move}.\n')
            file.write(f'Player chooses position {my_move}.\n')
            self.win_or_tie_check()
            self.computer_move()
        else:                                       # loop back, spot not empty
            print('That position is not empty, try again.')

    def ai_win_move(self):      # list of winning moves the AI can make
        ai_move = 0
        ''' Check move sets for a winning move to place. '''
        if (self.board.get(2) == self.computer_piece and self.board.get(3) == self.computer_piece and self.board.get(1) == ' ') or (self.board.get(4) == self.computer_piece and self.board.get(7) == self.computer_piece and self.board.get(1) == ' ') or (self.board.get(5) == self.computer_piece and self.board.get(9) == self.computer_piece and self.board.get(1) == ' '):
            ai_move = 1
        elif (self.board.get(1) == self.computer_piece and self.board.get(3) == self.computer_piece and self.board.get(2) == ' ') or (self.board.get(5) == self.computer_piece and self.board.get(8) == self.computer_piece and self.board.get(2) == ' '):
            ai_move = 2
        elif (self.board.get(1) == self.computer_piece and self.board.get(2) == self.computer_piece and self.board.get(3) == ' ') or (self.board.get(6) == self.computer_piece and self.board.get(9) == self.computer_piece and self.board.get(3) == ' ') or (self.board.get(5) == self.computer_piece and self.board.get(7) == self.computer_piece and self.board.get(3) == ' '):
            ai_move = 3
        elif (self.board.get(5) == self.computer_piece and self.board.get(6) == self.computer_piece and self.board.get(4) == ' ') or (self.board.get(1) == self.computer_piece and self.board.get(7) == self.computer_piece and self.board.get(4) == ' '):
            ai_move = 4
        elif (self.board.get(4) == self.computer_piece and self.board.get(6) == self.computer_piece and self.board.get(5) == ' ') or (self.board.get(2) == self.computer_piece and self.board.get(8) == self.computer_piece and self.board.get(5) == ' ') or (self.board.get(1) == self.computer_piece and self.board.get(9) == self.computer_piece and self.board.get(5) == ' ') or (self.board.get(3) == self.computer_piece and self.board.get(7) == self.computer_piece and self.board.get(5) == ' '):
            ai_move = 5
        elif (self.board.get(4) == self.computer_piece and self.board.get(5) == self.computer_piece and self.board.get(6) == ' ') or (self.board.get(3) == self.computer_piece and self.board.get(9) == self.computer_piece and self.board.get(6) == ' '):
            ai_move = 6
        elif (self.board.get(8) == self.computer_piece and self.board.get(9) == self.computer_piece and self.board.get(7) == ' ') or (self.board.get(1) == self.computer_piece and self.board.get(4) == self.computer_piece and self.board.get(7) == ' ') or (self.board.get(3) == self.computer_piece and self.board.get(5) == self.computer_piece and self.board.get(7) == ' '):
            ai_move = 7
        elif (self.board.get(2) == self.computer_piece and self.board.get(5) == self.computer_piece and self.board.get(8) == ' ') or (self.board.get(7) == self.computer_piece and self.board.get(9) == self.computer_piece and self.board.get(8) == ' '):
            ai_move = 8
        elif (self.board.get(7) == self.computer_piece and self.board.get(8) == self.computer_piece and self.board.get(9) == ' ') or (self.board.get(3) == self.computer_piece and self.board.get(6) == self.computer_piece and self.board.get(9) == ' ') or (self.board.get(1) == self.computer_piece and self.board.get(5) == self.computer_piece and self.board.get(9) == ' '):
            ai_move = 9
        return ai_move

    def ai_block_move(self):    # list of blocks the AI has to choose from
        ai_move = 0
        ''' Check move sets for a block move to place. '''
        if (self.board.get(2) == self.player_piece and self.board.get(3) == self.player_piece and self.board.get(1) == ' ') or (self.board.get(4) == self.player_piece and self.board.get(7) == self.player_piece and self.board.get(1) == ' ') or (self.board.get(5) == self.player_piece and self.board.get(9) == self.player_piece and self.board.get(1) == ' '):
            ai_move = 1
        elif (self.board.get(1) == self.player_piece and self.board.get(3) == self.player_piece and self.board.get(2) == ' ') or (self.board.get(5) == self.player_piece and self.board.get(8) == self.player_piece and self.board.get(2) == ' '):
            ai_move = 2
        elif (self.board.get(1) == self.player_piece and self.board.get(2) == self.player_piece and self.board.get(3) == ' ') or (self.board.get(6) == self.player_piece and self.board.get(9) == self.player_piece and self.board.get(3) == ' ') or (self.board.get(5) == self.player_piece and self.board.get(7) == self.player_piece and self.board.get(3) == ' '):
            ai_move = 3
        elif (self.board.get(5) == self.player_piece and self.board.get(6) == self.player_piece and self.board.get(4) == ' ') or (self.board.get(1) == self.player_piece and self.board.get(7) == self.player_piece and self.board.get(4) == ' '):
            ai_move = 4
        elif (self.board.get(4) == self.player_piece and self.board.get(6) == self.player_piece and self.board.get(5) == ' ') or (self.board.get(2) == self.player_piece and self.board.get(8) == self.player_piece and self.board.get(5) == ' ') or (self.board.get(1) == self.player_piece and self.board.get(9) == self.player_piece and self.board.get(5) == ' ') or (self.board.get(3) == self.player_piece and self.board.get(7) == self.player_piece and self.board.get(5) == ' '):
            ai_move = 5
        elif (self.board.get(4) == self.player_piece and self.board.get(5) == self.player_piece and self.board.get(6) == ' ') or (self.board.get(3) == self.player_piece and self.board.get(9) == self.player_piece and self.board.get(6) == ' '):
            ai_move = 6
        elif (self.board.get(8) == self.player_piece and self.board.get(9) == self.player_piece and self.board.get(7) == ' ') or (self.board.get(1) == self.player_piece and self.board.get(4) == self.player_piece and self.board.get(7) == ' ') or (self.board.get(3) == self.player_piece and self.board.get(5) == self.player_piece and self.board.get(7) == ' '):
            ai_move = 7
        elif (self.board.get(2) == self.player_piece and self.board.get(5) == self.player_piece and self.board.get(8) == ' ') or (self.board.get(7) == self.player_piece and self.board.get(9) == self.player_piece and self.board.get(8) == ' '):
            ai_move = 8
        elif (self.board.get(7) == self.player_piece and self.board.get(8) == self.player_piece and self.board.get(9) == ' ') or (self.board.get(3) == self.player_piece and self.board.get(6) == self.player_piece and self.board.get(9) == ' ') or (self.board.get(1) == self.player_piece and self.board.get(5) == self.player_piece and self.board.get(9) == ' '):
            ai_move = 9
        return ai_move

    def computer_move(self):    # AI player routine
        ''' Dumb'ish AI picker '''
        ai_move = random.randrange(1,10) # random 1-9
        block = self.ai_block_move()
        win = self.ai_win_move()
        if block != 0 or win != 0:
            if block > 0:       # if returned block_move value is greater than zero, play that move
                ai_move = block
            if win > 0:         # # if returned win_move value is greater than zero, play that move
                ai_move = win

        while self.board[ai_move] != ' ':        # stay here in a loop till an empty spot is picked
            if self.board[ai_move] != ' ':
                ai_move = random.randrange(1,10) # random 1-9
        else:                                    # AI plays a valid move
            self.board[ai_move] = self.computer_piece
            ttt.display_board()
            print(f'My move is position {ai_move}, now your move.')
            file.write(f'AI chooses position {ai_move}.\n')
            self.win_or_tie_check()
            self.player_move()

    def win_or_tie_check(self):         # routine both AI and player
        for set in self.winner_combos:
            total_moves = 0             # total move counter
            ai_score = 0                # ai score counter
            player_score = 0            # player score counter
            for key in set:             # step through combo sets
                if self.board[key] == self.computer_piece:  # does ai piece match a key value
                    ai_score += 1       # increment score counter
                if ai_score == 3:       # matched a complete set
                    print('I Win! Computers RULE, this player drools!\n')
                    file.write('I Win! Computers RULE, this player drools!\n')
                    file.close()
                    exit()
            for key in set:             # step through combo sets
                if self.board[key] == self.player_piece:    # does my piece match a key value
                    player_score += 1   # increment score counter
                if player_score == 3:   # matched a complete set
                    print('Congratulations, you won!\n')
                    file.write('Congratulations, you won!\n')
                    file.close()
                    exit()
            for key in self.board:      # step through board positions
                if self.board[key] == self.player_piece or self.board[key] == self.computer_piece:
                    total_moves += 1    # increment move counter
                if total_moves == 9:    # game was a tie
                    print('This game was a tie!\n')
                    file.write('This game was a tie!\n')
                    file.close()
                    exit()

ttt = TicTacToe()
ttt.player_decides()
