
from flask import request, jsonify
from create_player import players

def Create_team():
    #user enters the number required for each position category
    if request.method=="POST":
        nb_defenders = int(request.form["Enter the number of defenders:"])
        nb_midfielders= int(request.form["Enter the number of midfielders:"])
        nb_attackers= int(request.form["Enter the number of attackers"])

        #check if number of total players is 10, exit and print error if not 
        if nb_defenders+nb_attackers+nb_midfielders<10:
            return jsonify({"Error":"Not enough players"}),404
        else:
            #sort the players according to SET score in DESCENDING order
            sorted_players= sorted(players, key=lambda player: player.SET, reverse=True )

            #create new empty list for the 10 selected players
            selected_players=[]
            for player in sorted_players:
                if nb_defenders!=0 and player.position=="Defender":
                    nb_defenders=nb_defenders-1
                    selected_players.append(player)
                elif nb_midfielders!=0 and player.position=="Midfielder":
                    nb_midfielders=nb_midfielders-1
                    selected_players.append(player)
                elif nb_attackers!=0 and player.position=="Attacker":
                    nb_attackers= nb_attackers-1
                    selected_players.append(player)

            team=""
            for player in selected_players:
                team=team+str(player)

            return jsonify (team)
