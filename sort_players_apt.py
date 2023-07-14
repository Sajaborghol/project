from flask import jsonify
from create_player import players

def Sort_players_byAPT():
    sorted_players= sorted(players, key=lambda player: player.APT, reverse=True)
    sortedList=""
    for i in sorted_players:
        sortedList=sortedList+str(i)

    return jsonify(sortedList)