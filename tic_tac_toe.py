from random import choice

class Board:
    def __init__(self) -> None:
        self.board = [[str((num + (n * 3))) for num in range(3)] for n in range(3)]
        self.list = [i for i in range(9)]

    def check_win(self, turn_piece: str) -> bool:
        if [turn_piece, turn_piece, turn_piece] in self.board or \
                (self.board[0][0] == self.board[1][1] == self.board[2][2] == turn_piece) or \
                (self.board[2][0] == self.board[1][1] == self.board[0][2] == turn_piece) or \
                (self.board[0][0] == self.board[1][0] == self.board[2][0] == turn_piece) or \
                (self.board[0][1] == self.board[1][1] == self.board[2][1] == turn_piece) or \
                (self.board[0][2] == self.board[1][2] == self.board[2][2] == turn_piece):
            return True
        return False

    def __str__(self) -> str:
        return str(self.board)

    def __call__(self, number: int, piece: str, flag: bool = False) -> tuple:
        self.board[number // 3][number % 3] = piece
        if not flag:
            self.list.remove(number)
        if piece in ["X", "O"]:
            return self.check_win(piece), number
        else:
            self.list.append(number)
            self.list.sort()


class Player:
    def __init__(self, name: str, piece: str) -> None:
        self.user_name = name
        self.user_piece = piece


class Computer(Player):
    def __init__(self, name: str, piece: str) -> None:
        super().__init__(name, piece)

    @staticmethod
    def computer_choice(game_board: Board) -> tuple:
        for num in game_board.list:
            if not game_board(num, "X")[0]:
                game_board(num, str(num), True)
            else:
                return True, num
        for num in game_board.list:
            if game_board(num, "O")[0]:
                return game_board(num, "X", True)
            game_board(num, str(num), True)
        return game_board(choice(game_board.list), "X")


class Game:
    def __init__(self, player_number: int, gui) -> None:
        self.game_board = Board()
        Board.remaining_button_num = 9
        self.gui = gui
        self.player1 = Player("Player 1", "O")
        player_num = player_number
        if player_num == 2:
            self.player2 = Player("Player 2", "X")
        else:
            self.player2 = Computer("Computer", "X")


    def play(self):
        if self.player2.user_name == "Computer":
            if self.gui.turn_player_label.text() == "Turn player 2     X":
                winner, number = self.player2.computer_choice(self.game_board)
                self.gui.list_of_board_button[number].clicked_board(self.gui, winner)
