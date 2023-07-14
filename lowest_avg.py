
from flask import jsonify
from create_player import players
def lowest_AVG():
    average=10000
    for player in players:
        if ((player.APT+ player.SET)/2)<average:
            average= (player.APT+ player.SET)/2
            player_name= str(player.first_name) + str(player.last_name)
    return jsonify ("the player with lowest average is: " + player_name + "  " + "Average: " + str(average))       