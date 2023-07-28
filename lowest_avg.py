
from flask import jsonify
from create_player import players
from yourapp import get_database_connection
def lowest_AVG():

    average=100000

    db, cursor = get_database_connection()
    query ="SELECT id, first_name, last_name, APT,`SET`, national_association, position FROM players"
    cursor.execute(query)
    players=[]
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
        players.append(player)

    cursor.close()
    db.close()


    for player in players:
        if ((player["APT"]+player["SET"])/2 )< average:
            average= (player["APT"]+player["SET"])/2
            player_name= str(player["first_name"]) + str(player["last_name"])
    return jsonify ("the player with lowest average is: " + player_name + "  " + "Average: " + str(average))       