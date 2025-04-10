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
class Appearance:
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
class Game:
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
class League:
    leagueID: str
    name: str
    understatNotation: str

@dataclass
class Player:
    playerID: str
    name: str

@dataclass
class Shot:
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

#
#Use this function instead of reading in the file line by line
#this function will increase preformance and ease of use
# 
#file_path should be the relative path e.g. 'datasets/appearances.csv' 
#
#requested_class should be the name of the objects you want in your array, e.g. Appearance
#!!!THIS SHOULD NOT HAVE "" AROUND IT!!!
#
#to use this method in your program be sure to import at the top of your program
#import classes_for_dataset as cfd
#then call the function
#cfd.read_file_to_array('datasets/appearances.csv', Appearance)
#
#!!!DO NOT ALTER CODE BELOW!!!
#

def read_file_to_array(file_path:str, requested_class:object, filter_func=None, sort_key = None, requested_fields = None):
    
    with open(file_path, 'r') as f:
        csv_reader = csv.DictReader(f)

        requested_fields = requested_fields or [field for field in requested_class.__annotations__.keys()]


        def convert_row(row):
            new_row = {}
            for field, field_type in requested_class.__annotations__.items():
                if field in requested_fields:
                    value = row[field]

                    if field_type == int:
                        new_row[field] = int(value) if value.isdigit() else 0
                    elif field_type == float:
                        new_row[field] = float(value) if value.replace('.', '', 1).isdigit() else 0.0
                    elif field_type == dt.datetime:
                        new_row[field] = dt.datetime.strptime(value,"%Y-%m-%d %H:%M:%S") if value else None
                    else :
                        new_row[field] = value
            return requested_class(**new_row)

        array = [convert_row(row) for row in csv_reader if not filter_func or filter_func(row)]
    
    if sort_key:
        array.sort(key=sort_key)
    
    return array