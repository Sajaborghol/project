from flask import jsonify, request
from create_player import players

def calculate_avg():
    if request.method=="POST":
        firstName= request.form["Enter player's first name:"]
        lastName= request.form["Enter player's last name:"]
        for player in players:
            if player.first_name==firstName and player.last_name==lastName:
                average= (player.APT + player.SET)/2
                return jsonify(average)
            
    

    