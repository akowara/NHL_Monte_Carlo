for i in range(len(schedule.home)):
    print(schedule.home[i])
    print(schedule.visitor[i])
    homeGPG = getRosterGPG(schedule.home[i])
    visitorGPG = getRosterGPG(schedule.visitor[i])
    
    score = MonteCarlo(homeGPG, visitorGPG)
    if score>0:
        print(schedule.home[i] + " by: " + str(score))
    elif score<0:
        print(schedule.visitor[i] + " by: " + str(score))
    else:
        print("IT'S A TIE???")
    return app.send_static_file('index.html')