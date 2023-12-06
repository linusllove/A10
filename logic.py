import random

class TicTacToe:
    def __init__(self, single_player=False):
        self.board = self.get_empty_board()
        self.current_player = 'X'
        self.single_player = single_player
        self.bot = Bot() if single_player else None
        self.winner = None
        self.move_number = 0
        self.first_move = True
        self.first_move_position = None
    def get_empty_board(self):
        return [[None, None, None] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print(' | '.join([cell if cell is not None else ' ' for cell in row]))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_player_input(self):
        if self.current_player == 'O' and self.single_player:
            return self.bot.make_move(self.board)
        else:
            prompt = f"Player {self.current_player}, enter your move (row,col): "
            player_input = input(prompt)
            row_col_list = player_input.split(',')
            return [int(x) for x in row_col_list]

    def add_move_number(self):
        self.move_number += 1
        
    
        # with open('game_log.txt','a') as f:
        #     f.write(f'Winner is {winner} in {move_number} moves\n')
    def check_winner(self):
        # Checking rows for winner
        for row in self.board:
            if row[0] == row[1] == row[2] != None:
                self.winner = row[0]
                return row[0]

        # Checking columns for winner
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != None:
                self.winner = self.board[0][col]
                return self.board[0][col]

        # Checking diagonals for winner
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != None:
            self.winner = self.board[0][0]
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != None:
            self.winner = self.board[0][2]
            return self.board[0][2]

        # Check for a draw
        if all(all(row) for row in self.board):
            self.winner = "draw"
            return "draw"

        return None

    def play_game(self):
        winner = None
        while winner is None:
            self.print_board()
            try:
                row, col = self.get_player_input()
                if self.first_move:
                    print("First move")
                    self.first_move_position = (int(row), int(col))
                    self.first_move = False
                if self.board[row][col] is not None:
                    print("Spot taken, try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input, try again.")
                continue

            self.board[row][col] = self.current_player
            winner = self.check_winner()
            self.switch_player()

        self.print_board()
        if winner == "draw":
            print("It's a draw!")
        else:
            print(f"Winner is Player {winner}!")

class Bot:
    def make_move(self, board):
        empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
        return random.choice(empty_positions)


