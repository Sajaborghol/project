from flask import request, jsonify
from yourapp import get_database_connection
class Player:

#constructor
    def __init__ (self, ID, first_name, last_name, APT, SET, National_association, position):
        self.ID=ID
        self.first_name=first_name
        self.last_name=last_name
        self.APT=APT
        self.SET=SET
        self.National_association=National_association
        self.position=position
#method to print attributes for players
    def __str__(self):
        return f"ID: {self.ID}, Name: {self.first_name} {self.last_name}, position :{self.position},SET: {self.SET}, APT: {self.APT}, National association: {self.National_association}"

# create an emty list 
players =[]

iD=1
def Data_of_players():
    #user enters total nb of players
    global iD
    if request.method=="POST":
        data= request.get_json()

        first_name=data.get("Enter player's first name:")
        last_name=data.get("Enter player's last name:")
        APT= int(data.get("Enter player's APT:"))
        SET=  int(data.get("Enter player's SET:"))
        National_association=data.get("Enter player's national association:")
        position= data.get("Enter player's position:")

        db,cursor =get_database_connection()

        query ="INSERT INTO players (ID, first_name, last_name, APT, `SET`, National_association, position) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values= (int(iD), first_name, last_name, int(APT), int(SET), National_association, position)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()
        #create a player object and append it to the list
        players.append(Player(iD, first_name, last_name, APT, SET, National_association, position))
        #players.append(Player(iD, first_name, last_name, APT, SET, National_association,position))
        iD=iD+1
        return jsonify({"Message:":"Player Created Successfully"}),201