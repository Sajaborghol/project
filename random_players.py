from flask import request, jsonify
from create_player import players
import random 
def Random_players():

    NbOfPlayersRequired=int (request.form["Enter the number of players required"])

    if NbOfPlayersRequired>len(players):

        return jsonify({"Error":"Not enough players"}),404
    randomSampleOfPlayers= random.sample(players,int(NbOfPlayersRequired))
    rand_sample=""
    for i in randomSampleOfPlayers:
        rand_sample=rand_sample+ str(i)
    
    return jsonify(rand_sample)

    