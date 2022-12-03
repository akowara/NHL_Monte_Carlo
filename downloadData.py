import pandas as pd
from functions import abbriviation, getSchedule

#download FULL NHL schedule to csv
#def downloadSchedule():
#    url = "https://www.hockey-reference.com/leagues/NHL_2023_games.html#games"
#    html_content = pd.read_html(url)
#    df = html_content[0]
#    df.to_csv("csv/schedule.csv")


def downloadRosterGPG(teamName):
    url = "https://www.hockey-reference.com/teams/" + abbriviation(teamName) + "/2023.html#skaters"
    html_content = pd.read_html(url)
    roster = html_content[4]
    if hasattr(roster, 'Goalie Stats'):
        roster = html_content[3]
    roster.to_csv("csv/"+teamName+"_roster.csv")

schedule = getSchedule()

for i in range(len(schedule.home)):
    downloadRosterGPG(schedule.home[i])
    downloadRosterGPG(schedule.visitor[i])
#    homeGPG = getRosterGPG(schedule.home[i])
#    visitorGPG = getRosterGPG(schedule.visitor[i])
#    
#    score = MonteCarlo(homeGPG, visitorGPG)
#    if score>0:
#        print(schedule.home[i] + " by: " + str(score))
#    elif score<0:
#        print(schedule.visitor[i] + " by: " + str(score))
#    else:
#        print("IT'S A TIE???")