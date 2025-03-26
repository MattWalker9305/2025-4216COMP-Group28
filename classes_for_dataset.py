import csv
from dataclasses import dataclass
import datetime as dt

@dataclass
class TeamStatistic:
    gameID: str
    teamID: str
    season: str
    date: dt.datetime
    location: str
    goals: int
    xGoals: float
    shots: int
    shotsOnTarget: int
    deep: int
    ppda: float
    fouls: int
    corners: int
    yellowCards: int
    redCards: int
    result: str

@dataclass
class Team:
    teamID: str
    name: str

@dataclass
class appearance:
    gameID: str
    playerID: str
    goals: int
    ownGoals: int
    shots: int
    xGoals: float
    xGoalsChain: float
    xGoalsBuildup: float
    assists: int
    keyPasses: int
    xAssists: float
    position: str
    positionOrder: int
    yellowCard: int
    redCard: int
    time: int
    substituteIn: str
    substituteOut: str
    leagueID: str

@dataclass
class game:
    gameID: str
    leagueID: str
    season: str
    date: dt.datetime
    homeTeamID: str
    awayTeamID: str
    homeGoals: int
    awayGoals: int
    homeProbability: float
    drawProbability: float
    awayProbability: float
    homeGoalsHalfTime: int
    awayGoalsHalfTime:int
    B365H: float
    B365D: float
    B365A: float
    BWH: float
    BWD: float
    BWA: float
    IWH: float
    IWD: float
    IWA: float
    PSH: float
    PSD: float
    PSA: float
    WHH: float
    WHD: float
    WHA: float
    VCH: float
    VCD: float
    VCA: float
    PSCH: float
    PSCD: float
    PSCA: float

@dataclass
class league:
    leagueID: str
    name: str
    understatNotation: str

@dataclass
class player:
    playerID: str
    name: str

class shot:
    gameID: str
    shooterID: str
    assisterID: str
    minute: int
    situation: str
    lastAction: str
    shotType: str
    shotResult: str
    xGoal: float
    positionX: float
    positionY: float

def read_file_to_array(file_path:str, requested_class:object):
    with open(file_path, 'r') as f:
        csv_reader = csv.DictReader(f)
        array = [requested_class(**row) for row in csv_reader]
    return array