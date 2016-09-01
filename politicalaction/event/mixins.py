import csv

from .models import Event

def createEvents():
    events = csv.DictReader(open('static/csv/meetings.csv', 'r'))
    for event in events:
    	new_event = Event.objects.create(title=event["\xef\xbb\xbfName"], date=event[" Meeting Date "], time=event["Meeting Time"], location=event["Meeting Location"])
    	new_event.save()