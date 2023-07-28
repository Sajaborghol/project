from flask import request, jsonify
import random
from yourapp import get_database_connection
def Random_players():

    db,cursor =get_database_connection()

    query ="SELECT id, first_name, last_name, APT,`SET`, national_association, position FROM players"
    cursor.execute(query)
    all_players= cursor.fetchall()

    NbOfPlayersRequired=int (request.form["Enter the number of players required"])

    if NbOfPlayersRequired>len(all_players):

        return jsonify({"Error":"Not enough players"}),404
    

    randomSampleOfPlayers= random.sample(all_players,int(NbOfPlayersRequired))

    cursor.close()
    db.close()
    rand_sample=""
    for i in randomSampleOfPlayers:
        rand_sample=rand_sample+ str(i)
    
    return jsonify(rand_sample)

    