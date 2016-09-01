import csv

from .models import LegislativeBody

def createLegBody():
    legistaltivebodies = csv.DictReader(open('static/csv/leg_bodies.csv', 'r'))
    for leg_body in legistaltivebodies:
    	new_leg_body= LegislativeBody.objects.create(name=leg_body[" Legislative Body "])
    	new_leg_body.save()