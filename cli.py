from logic import TicTacToe
import logging
import os
def setup_logging():
    logging.basicConfig(filename='game_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')
    
def log_move(player, row, col):
    logging.info(f"Player {player} made a move to ({row}, {col})")

def choose_game_mode():
    while True:
        try:
            mode = int(input("Choose game mode (1 for single-player, 2 for two-player): "))
            if mode in [1, 2]:
                return mode == 1
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    setup_logging()
    single_player = choose_game_mode()
    game = TicTacToe(single_player)

    winner = None
    while winner is None:
        game.print_board()
        try:
            row, col = game.get_player_input()
            
            
            if game.board[row][col] is not None:
                print("Spot taken, try again.")
                
                continue
            else:
                if game.first_move:
                    game.first_move_position = (int(row), int(col))
                    game.first_move = False
                game.add_move_number()
                log_move(game.current_player, row, col)
        except (ValueError, IndexError):
            print("Invalid input, try again.")
            continue

        game.board[row][col] = game.current_player
        winner = game.check_winner()
        game.switch_player()

    game.print_board()
    if winner == "draw":
        logging.info("Game ended in a draw.")
        print("It's a draw!")
    else:
        logging.info(f"Winner is Player {winner}")
        print(f"Winner is Player {winner}!")
        
    if not os.path.exists('database.csv'):
        with open('database.csv', 'w') as f:
            f.write('move_number,winner,single_player,first_move_loc\n')
    
    with open('database.csv', 'a') as f:
        f.write(f"{game.move_number},{winner},{single_player},{game.first_move_position[0]*3+game.first_move_position[1]}\n")
        # f.write(f"{game.move_number},{winner},{single_player}\n")

if __name__ == "__main__":
    main()
