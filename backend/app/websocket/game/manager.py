from app.websocket.game.state import ChessState


class GameManager:

    def __init__(self):

        self.games = {}


    def create_game(
        self,
        room_id,
        players
    ):
        if room_id in self.games:
            return self.games[room_id]

        game = ChessState(room_id)

        game.players["white"] = players[0]
        game.players["black"] = players[1]

        self.games[room_id] = game

        return game


    def get_game(
        self,
        room_id
    ):

        return self.games.get(room_id)


    def remove_game(
        self,
        room_id
    ):

        if room_id in self.games:
            del self.games[room_id]


game_manager = GameManager()