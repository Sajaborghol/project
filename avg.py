from flask import jsonify, request
from create_player import players
from yourapp import get_database_connection

def calculate_avg():
    if request.method=="POST":
        firstName= request.form["Enter player's first name:"]
        lastName= request.form["Enter player's last name:"]
        db,cursor =get_database_connection()
        query ="SELECT id, first_name, last_name, APT,`SET`, national_association, position FROM players"
        cursor.execute(query)
        for row in cursor.fetchall():

            player={
            "id":row[0],
            "first_name": row[1],
            "last_name": row[2],
            "APT": row[3],
            "SET":row[4],
            "national_association":row[5],
            "position":row[6]
            }
            if player["first_name"]==firstName and player["last_name"]==lastName:
                average= (player["APT"] + player["SET"])/2
                return jsonify(average)
            

        cursor.close()
        db.close()

            
    

    