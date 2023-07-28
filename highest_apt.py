from create_player import players
from flask import jsonify
from yourapp import get_database_connection
def highestAPT():

    db, cursor = get_database_connection()
    query ="SELECT id, first_name, last_name, APT,`SET`, national_association, position FROM players"
    cursor.execute(query)

    players=[]
    for row in cursor.fetchall():
        player = {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "APT": row[3],
            "SET": row[4],
            "national_association": row[5],
            "position": row[6]
        }
        players.append(player)
    cursor.close()
    db.close()

    sorted_players= sorted(players, key=lambda player: player["APT"], reverse=True)
    highest_APT = sorted_players[0]
    highestAPT= str(highest_APT)
    return jsonify(highestAPT)
