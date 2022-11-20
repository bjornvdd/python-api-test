

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# implementing security
origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://bjornvdd.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 1ste basemodel voor player
class Player(BaseModel):
    first_name: str | None = "Invalid"
    last_name: str | None = "Invalid"
    email: str | None = None
    number: int | None = "Invalid"
    birth_date: str | None = None


# 2de basemodel voor team
class Team(BaseModel):
    team_name: str | None = "Invalid"
    captain_team: str | None = None
    played_games: int | None = "Invalid"
    ranking: int | None = "Invalid"


team_real_madrid = {
    "team_name": "Real Madrid",
    "captain_team": "Luka Modric",
    "played_games": 6,
    "ranking": 7
}

team_liverpool = {
    "team_name": "Liverpool",
    "captain_team": "Mohammed Salah",
    "played_games": 5,
    "ranking": 3
}
team_manchester_united = {
    "team_name": "Manchester United",
    "captain_team": "Paul Pogba",
    "played_games": 4,
    "ranking": 4
}
team_southampton = {
    "team_name": "Southampton FC",
    "captain_team": "James Ward-Prowse",
    "played_games": 5,
    "ranking": 2
}

team_chelsea = {
    "team_name": "Chelsea",
    "captain_team": "Lampard",
    "played_games": 6,
    "ranking": 1
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

team_list = [team_real_madrid, team_manchester_united, team_chelsea, team_liverpool, team_southampton]
player_list = [first_player, second_player, third_player]


@app.post("/make/player", response_model=Player)
async def create_player(player: Player):
    return player


@app.get("/teams/{ranking_position}", response_model=Team)
async def get_teams(ranking_position: int):
    for team in team_list:
        if team.get("ranking") == ranking_position: #een team opvragen op basis waarvan ze staan in het klassement (bv. 1e,2e,3e plaats)
            return team
   


@app.get("/player/{player_name}", response_model=Player)
async def get_player(player_name: str):
    for player in player_list:
        if player.get(
                "first_name") == player_name:  # kijkt naar de firstname van de speler en geeft dan bijkomende informatie erbij
            return player
    return "Speler niet mogelijk"
