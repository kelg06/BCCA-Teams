from django.shortcuts import render
from django.http import HttpResponse
from dataclasses import dataclass
@dataclass
class Team:
    name:str
    desc:str
    memb:list


pro_team=Team("Procurement",
    "Procurement team buy's food to cook so that they can feed the students at lunch time and they buy supplies like soap, trash, bags etc",
    ['Markel', 'Arthur', 'Jacob', 'Aaron'])
teams = {
    "Procurement": pro_team
}

pro_name = teams["Procurement"].name
pro_desc = teams["Procurement"].desc
pro_memb = teams["Procurement"].memb





com_team=Team("Community",
    "Their job is to plan events that bring people together, build lasting relationships, and promote engagement.",
    ['Arianna', 'Peyton'])
teams = {
    "Community": com_team
}
com_name = teams["Community"].name
com_desc = teams["Community"].desc
com_memb = teams["Community"].memb




doc_team=Team("Documentation",
    "Documentation team is responsible for taking photos of guest speaker, community events , and unit projects after taking the pictures depending on the event happening in the photos determines which social media we post on we are also responsible for getting all the photos for the year book.",
    ['Patrick', 'Jason'])
teams = {
    "Documentation": doc_team
}
doc_name = teams["Documentation"].name
doc_desc = teams["Documentation"].desc
doc_memb = teams["Documentation"].memb




man_team=Team("Documentation",
    """Cleaning the kitchen, and taking out the trash.
        Sweeping the main lobby and also sweeping the backhallway/classrooms.
        Wiping all the tables, including the kitchen tables.""",
    ['Chris', 'Tanner','Aidan','Kilan'])
teams = {
    "Management": man_team
}
man_name = teams["Management"].name
man_desc = teams["Management"].desc
man_memb = teams["Management"].memb

def root_view(request):
    context={
        "name":["Management","Documentation","Community","Procurement"]
    }
    return render(request,"home.html",context)



def team_view(request,teams):
    if teams =="Management":
        team_context = {
        "name" : man_name,
        "desc": man_desc,
        "memb": man_memb,
    }
    elif teams =="Documentation":
        team_context = {
        "name" : doc_name,
        "desc": doc_desc,
        "memb": doc_memb,
    }
    elif teams =="Community":
        team_context = {
        "name" : com_name,
        "desc": com_desc,
        "memb": com_memb,
    }
    elif teams == "Procurement":
        team_context = {
        "name" : pro_name,
        "desc": pro_desc,
        "memb": pro_memb,
    }
    return render(request,"teams.html", team_context)



    