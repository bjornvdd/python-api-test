from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Player(BaseModel):
    first_name: str | None = "Invalid"
    last_name: str | None = "Invalid"
    email: str | None = None
    number: int | None = "Invalid"
    birth_date: str | None = None


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

team_list = [team_real_madrid, team_manchester_united]
player_list = [first_player, second_player, third_player]


@app.post("/player", response_model=Player)
async def create_player(player: Player):
    return player


@app.get("/teams", response_model=list)
async def get_teams():
    return team_list


@app.get("/player/{player_name}", response_model=Player)
async def get_player(player_name: str):
    for player in player_list:
        if player.get("first_name") == player_name:
            return player
    return "Speler niet mogelijk"
