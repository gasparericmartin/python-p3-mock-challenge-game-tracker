#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    game = Game('Gow')
    player = Player("Nick")
    player_2 = Player("Ari")
    Result(player, game, 5000)
    Result(player, game, 5002)
    Result(player_2, game, 4999)

    ipdb.set_trace()
