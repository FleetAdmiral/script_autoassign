import csv
import random

class student:
    team_no = ""
    preferences=[]
    final_project = ""

teamList = []
listProjects = []
finalSelect = {}

with open('italloc.csv', 'rb') as italloc:
    reader = csv.DictReader(italloc)

    for r in reader:
        team = student()
        team.team_no=r["Team Number"]
        pref_now =[]
        for k in range(1,11):
            pref=r["Preference "+str(k)]
            if pref not in listProjects:
                listProjects.append(pref)
            pref_now.append(pref)
        team.preferences = pref_now
        teamList.append(team)

    for lp in listProjects:
        whoSelected =[]
        whoSelectedF = []
        for tl in teamList:
            if(tl.preferences[0]==lp):
                whoSelected.append(tl)
        if(len(whoSelected)>4):
            for select in range(4):
                sel = random.choice(whoSelected)
                whoSelected.remove(sel)
                whoSelectedF.append(sel)
            for all in whoSelected:
                all.preferences.pop(0)
        else:
            whoSelectedF = whoSelected

        for all in whoSelectedF:
            teamList.remove(all)

        finalSelect[lp]=whoSelectedF

for all in finalSelect:
    print all + ": "
    for alli in finalSelect[all]:
        print alli.team_no
