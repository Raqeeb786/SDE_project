class ChessState:

    def __init__(self, room_id):

        self.room_id = room_id

        self.players = {
            "white": None,
            "black": None
        }

        self.turn = "white"

        self.board = self.create_board()

        self.moves = []


    def create_board(self):

        return [
            ["r","n","b","q","k","b","n","r"],
            ["p","p","p","p","p","p","p","p"],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["P","P","P","P","P","P","P","P"],
            ["R","N","B","Q","K","B","N","R"]
        ]