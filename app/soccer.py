from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Player(BaseModel):
    first_name: str
    last_name: str
    email: str | None = None
    number: int
    birth_date: str | None = None


class Team(BaseModel):
    team_name: str
    captain_team: str
    played_games: int
    ranking: int


team_real_madrid = {
    "team_name": "Real Madrid",
    "captain_team": "Luka Modric",
    "played_games": 6,
    "ranking": 7
}
team_manchester_united = {
    "team_name": "Manchester United",
    "captain_team": "Paul Pogba",
    "played_games": 5,
    "ranking": 4
}

first_player = {
    "first_name": "Cristiano",
    "last_name": "Ronaldo",
    "email": "cr7@email.com",
    "number": 7,
    "birth_date": "5/02/1985"

}

second_player = {
    "first_name": "Kevin",
    "last_name": "De Bruyne",
    "email": "kevindebruyne@email.com",
    "number": 10,
    "birth_date": "15/04/1982"

}

third_player = {
    "first_name": "Karim",
    "last_name": "Benzema",
    "email": "karimbenzema@email.com",
    "number": 9,
    "birth_date": "14/10/1998"

}

team = {0: team_real_madrid, 1: team_manchester_united}
player = {1: first_player}
player_list = [first_player, second_player, third_player]


@app.post("/player")
async def create_player(player: Player):
    return player


@app.get("/team")
async def get_team():
    return team


@app.get("/player/{player_name}")
async def get_player(player_name):
    for player in player_list:
        if player.get("first_name") == player_name:
            return player
    return "Speler niet mogelijk"
