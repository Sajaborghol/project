

from flask import jsonify
from create_player import players
from yourapp import get_database_connection
def Create_report():

    db,cursor =get_database_connection()
    query ="SELECT id, first_name, last_name, APT,`SET`, national_association, position FROM players"
    cursor.execute(query)

    #initialize positions
    attackers_count=0
    midfielders_count=0
    defenders_count=0


    

    for row in cursor.fetchall():
        player={
            "id":row[0],
            "first_name": row[1],
            "last_name": row[2],
            "APT": row[3],
            "SET": row[4],
            "national_association": row[5],
            "position": row[6]
        }

        if player["position"]=="Attacker":
            attackers_count+=1
        elif player["position"]=="Defender":
            defenders_count+=1
        elif player["position"]=="Midfielder":
            midfielders_count+=1
    cursor.close()
    db.close()
    print(midfielders_count)
    return jsonify("attackers: "+ str(attackers_count) +"  "+ "defenders: "+ str(defenders_count)+ "  "+ "midfielders: " + str(midfielders_count))