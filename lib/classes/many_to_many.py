class Game:
    def __init__(self, title):
        #check if the title has been set
        if hasattr(self, '_title'):
            raise AttributeError("Cannot modify the title once set")
        
        #validate title input
        if isinstance(title, str) and len(title) > 0:
            #set the title to a private attribute
            self._title = title
            self._results = []
        
        else:
            raise ValueError("Title must be a non-empty string")
        

    @property
    def title(self):
        return self._title

    def results(self):
        return self._results

    def players(self):
        players = {result.player for result in self._results}
        return list(players)

    def average_score(self, player):
        player_results = [result.score for result in self._results if result.player == player]
        if player_results:
            return sum(player_results) / len(player_results)
        return 0

class Player:
    def __init__(self, username):
        self._username = None #will hod actual username value
        self.username = username #call the property setter


        #store results for the player
        self._results = [] 

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._username = value
        
        else:
            raise ValueError("Username must be a string between 2 and 16 characters long.")

#    def username(self):
 #       return self.username
    def results(self):
        return self._results

    def games_played(self):
        games = {result.game for result in self._results}
        return list(games)

    def played_game(self, game):
        return any(result.game == game for result in self._results)
    

    def num_times_played(self, game):
        return sum(1 for result in self._results if result.game ==game)

class Result:
    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise TypeError("Player must be an instance of the player class")
        if not isinstance(game, Game):
            raise TypeError("game must be an instance of the Game class")
        self._player = player
        self._game = game
        self.score = score

        player._results.append(self)
        game.results().append(self)

    #property to return the player
    @property
    def player(self):
        return self._player

    #property to return game
    @property
    def game(self):
        return self._game

    #property for score            
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if hasattr(self, '_score'):
            raise AttributeError("Score cannot be changed onces set")
        if isinstance (value, int) and 1 <= value <= 5000:
            self._score = value
        else:
            raise ValueError("Score must be integer btn 1 and 5000")