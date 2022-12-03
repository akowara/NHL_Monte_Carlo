import urllib.request
import pandas as pd
from array import *
from datetime import datetime
from random import random
from html.parser import HTMLParser
from functions import *
import json

from flask import Flask, Response, request, jsonify, json
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/getScores')
def getScores():
    schedule = getSchedule()
    todaysGames = []
    for i in range(len(schedule)):
        homeGPG = getRosterGPG(schedule[i].home)
        visitorGPG = getRosterGPG(schedule[i].visitor)    
        score = MonteCarlo(homeGPG, visitorGPG)
        game = {
            "home": schedule[i].home,
            "visitor": schedule[i].visitor,
            "score": score,
            "date":schedule[i].date
        }
        todaysGames.append(game)
    return json.dumps(todaysGames)


if __name__ == '__main__':
    app.run(debug = True)

class Game:
    def __init__(self, home, visitor, score):
        self.home = home
        self.visitor = visitor
        self.score = score

