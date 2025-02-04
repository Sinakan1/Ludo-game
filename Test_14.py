import random
from colorama import Fore, init

init(autoreset=True)

def progress_to_abs(player, progress):
    """
    Given a player's progress on the main board (0 <= progress <= main_path_moves),
    compute the absolute board position (0-39).
    - progress == 0 means the piece is in the reserved starting square.
    - As the piece advances, reserved squares belonging to other players are skipped.
    """
    reserved = {1, 11, 21, 31}
    # If progress is 0, the piece is at its reserved square.
    if progress == 0:
        return player.start_house
    pos = player.start_house  # starting square (reserved) is the entry point.
    count = 0
    # Advance one square at a time until we have moved 'progress' non‐reserved steps.
    while count < progress:
        pos = (pos + 1) % 40
        # Skip the square if it is reserved for another player.
        if pos in reserved and pos != player.start_house:
            continue
        count += 1
    return pos

class Player:
    def __init__(self, name, color, start_house, symbol):
        self.name = name
        self.color = color
        self.symbol = symbol
        # Piece progress meaning:
        #   -1 : In the Start area (not yet in play)
        #  0 to main_path_moves (here 36): On the main board
        #  (main_path_moves + 1) to (main_path_moves + home_stretch_length) (i.e. 37 to 40):
        #         In the Home stretch (home house number = progress - main_path_moves)
        self.pieces = [-1] * 4
        self.start_house = start_house         # Reserved square for this player (1, 11, 21, or 31)
        self.main_path_moves = 36              # Number of moves required on the main board
        self.home_stretch_length = 4           # Number of Home houses

    def get_abs_position(self, piece_idx):
        """
        If a piece's progress is between 0 and main_path_moves (inclusive),
        return its absolute board position (0-39) on the main board.
        Otherwise (if in Home stretch or still in Start), return None.
        """
        progress = self.pieces[piece_idx]
        if progress == -1:
            return None  # Not yet in play
        if progress <= self.main_path_moves:
            return progress_to_abs(self, progress)
        return None  # In Home stretch

    def home_slot(self, piece_idx):
        """
        If the piece is in the Home stretch (progress > main_path_moves),
        return its home house number (1-indexed).
        Otherwise, return None.
        """
        progress = self.pieces[piece_idx]
        if progress > self.main_path_moves:
            return progress - self.main_path_moves
        return None

class Game:
    def __init__(self, num_players=2):
        # Set up players with their reserved starting squares.
        all_players = [
            Player("Player 1", Fore.RED, 1, "🔴"),
            Player("Player 2", Fore.BLUE, 11, "🔵"),
            Player("Player 3", Fore.GREEN, 21, "🟢"),
            Player("Player 4", Fore.YELLOW, 31, "🟡")
        ]
        self.players = all_players[:num_players]
        self.current_player = 0
        self.board = {}  # Maps board positions (0-39) to lists of (player_idx, piece_idx)
        self.num_players = num_players

    def update_board(self):
        """
        Update the dictionary mapping main board positions to the pieces on them.
        Only pieces with progress between 0 and main_path_moves (inclusive) appear on the board.
        """
        self.board = {}
        for p_idx, player in enumerate(self.players):
            for pc_idx, prog in enumerate(player.pieces):
                abs_pos = player.get_abs_position(pc_idx)
                if abs_pos is not None and prog <= player.main_path_moves:
                    if abs_pos not in self.board:
                        self.board[abs_pos] = []
                    self.board[abs_pos].append((p_idx, pc_idx))

    def validate_move(self, player_idx, piece_idx, steps):
        """
        Validate whether a move is legal:
         - A piece in Start (-1) may only leave on a roll of 6.
         - A move must not overshoot the final home house.
         - When moving on the main board (progress ≤ main_path_moves), the destination square must not be
           already occupied by another of the player's pieces.
         - When moving in the Home stretch, the destination home house must be free.
        """
        player = self.players[player_idx]
        current_prog = player.pieces[piece_idx]

        # If the piece is in Start, it may only leave on a 6.
        if current_prog == -1:
            return steps == 6

        new_prog = current_prog + steps
        max_prog = player.main_path_moves + player.home_stretch_length  # For example, 36 + 4 = 40
        if new_prog > max_prog:
            return False  # Overshooting the final home house

        # Check for collisions if the piece is moving on the main board.
        if new_prog <= player.main_path_moves:
            new_abs = progress_to_abs(player, new_prog)
            for idx, prog in enumerate(player.pieces):
                if idx == piece_idx or prog == -1:
                    continue
                if prog <= player.main_path_moves and progress_to_abs(player, prog) == new_abs:
                    return False
        else:
            # Moving into the Home stretch.
            home_house = new_prog - player.main_path_moves  # Home house number (1-indexed)
            # Ensure no other piece of the same player is in that home house.
            for idx, prog in enumerate(player.pieces):
                if idx == piece_idx or prog <= player.main_path_moves:
                    continue
                if (prog - player.main_path_moves) == home_house:
                    return False

        return True

    def move_piece(self, player_idx, piece_idx, steps):
        player = self.players[player_idx]
        if not self.validate_move(player_idx, piece_idx, steps):
            print("Invalid move!")
            return False

        # If the piece is in Start, a 6 brings it onto the main board (progress becomes 0).
        if player.pieces[piece_idx] == -1:
            player.pieces[piece_idx] = 0
        else:
            player.pieces[piece_idx] += steps

        self.update_board()
        # Only check for collisions if the piece remains on the main board.
        abs_pos = player.get_abs_position(piece_idx)
        if abs_pos is not None:
            self.check_collision(abs_pos, player_idx)
        return True

    def check_collision(self, position, current_player_idx):
        """
        On the main board, if a piece lands on a square occupied by an opponent's piece,
        that opponent's piece is sent back to Start.
        (No collisions occur in the Home stretch.)
        """
        if position is None or position >= 40:
            return

        if position in self.board:
            for (p_idx, pc_idx) in self.board[position]:
                if p_idx != current_player_idx:
                    print(f"{self.players[p_idx].name}'s piece returned to start!")
                    self.players[p_idx].pieces[pc_idx] = -1
            self.update_board()

    def has_won(self, player_idx):
        """
        A player wins when all 4 of their pieces have entered the Home stretch.
        (i.e. when each piece's progress is greater than main_path_moves)
        """
        player = self.players[player_idx]
        return all(prog > player.main_path_moves for prog in player.pieces)

    def print_board(self):
        print("\n" + "=" * 40)
        print(f"{' CURRENT GAME STATUS ':^40}")
        print("=" * 40)

        # Start Area
        print("\n📦 Start Area:")
        for player in self.players:
            count = sum(1 for prog in player.pieces if prog == -1)
            if count:
                print(f"{player.color}{player.name}: {count} piece(s)")

        # Reserved Starting Houses (on the main board)
        print("\n🏠 Reserved Starting Houses (on main board):")
        for player in self.players:
            count = sum(1 for prog in player.pieces if prog == 0)
            if count:
                print(f"{player.color}{player.name} (House {player.start_house}): {count} piece(s)")

        # Main Board Path (positions 0-39)
        print("\n🛣️ Main Board:")
        main_path = []
        reserved_positions = {1, 11, 21, 31}
        for i in range(40):
            if i in reserved_positions:
                # For a reserved square, display the player's symbol if occupied; otherwise, a black square.
                found = False
                for p_idx, player in enumerate(self.players):
                    for prog in player.pieces:
                        if prog == 0 and player.start_house == i:
                            main_path.append(player.symbol)
                            found = True
                            break
                    if found:
                        break
                if not found:
                    main_path.append("⬛")
            else:
                if i in self.board:
                    p_idx, _ = self.board[i][0]
                    main_path.append(self.players[p_idx].symbol)
                else:
                    main_path.append("⬜")
        for i in range(0, 40, 10):
            print(" ".join(main_path[i:i+10]))

        # Home Stretch for each player (the 4 home houses that continue the journey)
        print("\n🏡 Home Stretch Areas:")
        for player in self.players:
            # Create a list for home houses: empty slot shown as ⬜.
            home_houses = ["⬜"] * player.home_stretch_length
            for prog in player.pieces:
                if prog > player.main_path_moves:
                    slot = prog - player.main_path_moves  # home house number (1-indexed)
                    if 1 <= slot <= player.home_stretch_length:
                        home_houses[slot - 1] = player.symbol
            print(f"{player.color}{player.name}: {' '.join(home_houses)}")

        # Detailed Piece Status
        print("\n🔍 Detailed Piece Status:")
        for player in self.players:
            print(f"\n{player.color}{player.name}:")
            for idx, prog in enumerate(player.pieces):
                if prog == -1:
                    status = "Start"
                elif prog <= player.main_path_moves:
                    abs_pos = progress_to_abs(player, prog)
                    status = f"Main Board {abs_pos} (Progress {prog})"
                else:
                    slot = prog - player.main_path_moves
                    status = f"Home House {slot}"
                print(f"Piece {idx}: {status}")

    def roll_dice(self):
        return random.randint(1, 6)

    def play_turn(self):
        player = self.players[self.current_player]
        print(f"\n{player.color}{player.name}'s Turn")
        input("Press Enter to roll the dice...")
        dice = self.roll_dice()
        print(f"Dice rolled: {dice}")

        movable = []
        for i, prog in enumerate(player.pieces):
            # A piece in Start (-1) may only leave with a 6.
            if prog == -1 and dice == 6:
                movable.append(i)
            # Otherwise, if the piece is on the main board or in the Home stretch,
            # check if the move is valid.
            elif prog != -1 and prog < (player.main_path_moves + player.home_stretch_length) and \
                 self.validate_move(self.current_player, i, dice):
                movable.append(i)

        if not movable:
            print("No movable pieces!")
            self.current_player = (self.current_player + 1) % self.num_players
            return False

        print("Movable pieces:", movable)
        while True:
            try:
                choice = int(input("Select piece (0-3): "))
                if choice in movable:
                    break
                print("Invalid selection!")
            except ValueError:
                print("Please enter a number between 0-3!")

        if self.move_piece(self.current_player, choice, dice):
            if self.has_won(self.current_player):
                print(f"{player.name} WINS! 🎉")
                return True
            if dice != 6:
                self.current_player = (self.current_player + 1) % self.num_players
            else:
                print("Extra turn granted!")
        return False

def main_menu():
    """Display the main menu and prompt the user for a choice."""
    while True:
        print("\n" + "=" * 40)
        print(" MAIN MENU ".center(40, "="))
        print("=" * 40)
        print("1. New Game   - Start a new game session.")
        print("2. How To Play - Learn how to play the game.")
        print("3. Exit       - Quit the game.")
        choice = input("Select an option (1-3): ")
        if choice == "1":
            return "new_game"
        elif choice == "2":
            how_to_play()
        elif choice == "3":
            exit_game()
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

def how_to_play():
    """Display a short explanation on how to play the game."""
    print("\nHow To Play:")
    print("New Game: Starts a new game session. You'll be asked for the number of players (2-4) and then take turns rolling the dice and moving your pieces.")
    print("How To Play: Displays this help information so you understand the controls and objectives.")
    print("Exit: Quits the game.")
    input("\nPress Enter to return to the main menu...")

def exit_game():
    """Exit the game."""
    print("\nExiting the game. Goodbye!")
    exit()

def main():
    while True:
        option = main_menu()
        if option == "new_game":
            while True:
                try:
                    num_players = int(input("\nEnter number of players (2-4): "))
                    if 2 <= num_players <= 4:
                        break
                    print("Please enter 2, 3, or 4.")
                except ValueError:
                    print("Invalid input! Please enter a number.")
            game = Game(num_players)
            while True:
                game.print_board()
                if game.play_turn():
                    game.print_board()
                    print("GAME OVER!")
                    break
            input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main()
