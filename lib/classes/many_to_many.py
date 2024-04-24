class Game:

    all = []
    
    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, 'title') and title:
            self._title = title
        else:
            raise Exception("There's a problem")

    def results(self):
        return [result for result in Result.all if self == result.game]

    def players(self):
        final_set = []
        init_set = [result.player for result in Result.all if self == result.game]

        for player in init_set:
            if player not in final_set:
                final_set.append(player)
        
        return final_set
        

    def average_score(self, player):
        scores = [result.score for result in Result.all if result.game == self and result.player == player]
        total = 0
        for score in scores:
            total += score
        
        avg = total / len(scores)
        return avg

class Player:
    
    all = []
    
    def __init__(self, username):
        self.username = username
        Player.all.append(self)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str):
            if len(username) >= 2 and len(username) <= 16:
                self._username = username


    def results(self):
        return [result for result in Result.all if self == result.player]


    def games_played(self):
        export_list = []
        full_list = [result.game for result in Result.all if self == result.player]

        for game in full_list:
            if game not in export_list:
                export_list.append(game)
        
        return export_list
    

    def played_game(self, game):
        if self in [result.player for result in Result.all if game == result.game]:
            return True
        else:
            return False

    def num_times_played(self, game):
        return len([result for result in Result.all if game == result.game and self == result.player])

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and not hasattr(self, 'score') and 1<= score <= 5000:
            self._score = score
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        self._player = player
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        self._game = game
