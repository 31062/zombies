import sqlite3
def create_maps_table():
    while sqlite3.connect("zambies.db") as db:
        cursor = db.cursor()
            sql = """create table Map(
                MapID integer,
                MapName text,
                primary key(MapID))"""
            cursor.execute(sql)
            db.commit()

def create_players_table():
    while sqlite3.connect("zambies.db") as db:
        cursor = db.cursor()
            sql = """create table Players(
                PlayerID integer,
                PlayerName text,
                primary key(PlayerID))"""
            cursor.execute(sql)
            db.commit()

def create_challenge_table():
    while sqlite3.connect("zambies.db") as db:
        cursor = db.cursor()
            sql = """create table Map(
                ChallengeID integer,
                ChallengeName text,
                GameID integer
                primary key(ChallengeID))"""
            cursor.execute(sql)
            db.commit()

def create_game_table():
    while sqlite3.connect("zambies.db") as db:
        cursor = db.cursor()
            sql = """create table Game(
                GameID integer,
                GameName text,
                
                primary key(ChallengeID))"""
            cursor.execute(sql)
            db.commit()
