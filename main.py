from create_player import Data_of_players
from random_players import Random_players
from sort_players_apt import Sort_players_byAPT
from highest_apt import highestAPT
from create_team import Create_team
from avg import calculate_avg
from lowest_avg import lowest_AVG
from report import Create_report
from flask import Flask

app=Flask(__name__)

@app.route('/create_player', methods=["POST"])
def handle_player():
    return Data_of_players()

@app.route('/random_players', methods=["POST"])
def handle_random():
    return Random_players()

@app.route('/sort_players_apt', methods=["GET"])
def handle_sort_apt():
    return Sort_players_byAPT()

@app.route('/highest_apt', methods=["GET"])
def handle_highest_apt():
    return highestAPT()

@app.route('/create_team', methods=["POST"])
def handle_create_team():
    return Create_team()

@app.route('/avg', methods=["POST"])
def handle_avg():
    return calculate_avg()


@app.route('/lowest_avg', methods=["GET"])
def handle_lowest_avg():
    return lowest_AVG()

@app.route('/report', methods=["GET"])
def handle_report():
    return Create_report()

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True)
