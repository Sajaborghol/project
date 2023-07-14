from create_player import players
from flask import jsonify
def highestAPT():

    sorted_players= sorted(players, key=lambda player: player.APT, reverse=True)
    highest_APT = sorted_players[0]
    highestAPT= str(highest_APT)
    return jsonify(highestAPT)
