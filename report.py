

from flask import jsonify
from create_player import players
def Create_report():

    #initialize positions
    attackers_count=0
    midfielders_count=0
    defenders_count=0
    for player in players:
        if player.position=="Attacker":
            attackers_count+=1
        elif player.position=="Defender":
            defenders_count+=1
        elif player.position=="Midfielder":
            midfielders_count=+1

    return jsonify("attackers: "+ str(attackers_count) +"  "+ "defenders: "+ str(defenders_count)+ "  "+ "midfielders: " + str(midfielders_count))