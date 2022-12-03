import pandas as pd
from array import *
from datetime import datetime
from random import random

class TodaysGame:
    def __init__(self, home, visitor, date):
        self.home = home
        self.visitor = visitor
        self.date = date

class TeamStats:
    def __init__(self, gfg, gag):
        self.gfg = gfg
        self.gag = gag

def getSchedule():
    df = pd.read_csv('csv/schedule.csv')
    todaysSchedule = []
    for i in df.index:
        if df['Date'][i] == datetime.today().strftime('%Y-%m-%d') :
            todaysSchedule.append(TodaysGame(df['Home'][i],df['Visitor'][i],df['Date'][i]))
    return todaysSchedule

def getRosterGPG(teamName):
    roster = pd.read_csv("csv/"+teamName+"_roster.csv", header=1)
    goalsFor = roster["G"][len(roster["G"])-1]
    teamGP = roster["GP"][len(roster["GP"])-1]
    gamesPlayed = sum(roster["GP"]) - 2*teamGP
    gpg = goalsFor/gamesPlayed
    return round(gpg, 2)

def abbriviation(name):
    df = pd.read_csv('csv/team_abbrev.csv')
    for row in df.itertuples():
        if row.TeamName == name:
            return row.Abbrev

def CalculateNumberOfGoals(gpg):
    count = 0
    for i in range(16):
        randomNum = random()
        if gpg>randomNum:
            count = count+1
    return count

def MonteCarlo(homeGPG, visitorGPG):
    count = 0
    for i in range(10000):
        homeScore = CalculateNumberOfGoals(homeGPG)
        visitorScore = CalculateNumberOfGoals(visitorGPG)
        if homeScore>visitorScore:
            count = count + 1
        elif homeScore<visitorScore:
            count = count - 1
    return count
