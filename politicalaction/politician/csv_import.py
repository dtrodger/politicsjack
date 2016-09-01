import csv

from .models import Politician

def createMembers():
    politicians = csv.DictReader(open('static/csv/members.csv', 'r'))
    for member in politicians:
    	new_politician = Politician.objects.create(name=member[" Person Name "], ward=member["Ward/Office"], phone=member["Ward Office Phone"], fax=member["Fax"], email=member["E-mail"], website=member["Web Site"], office_address=member["Ward Office Address"], office_city=member["City"], office_state=member["State"], office_zip=member["Zip"], city_hall_phone=member["City Hall Phone"], city_hall_address=member["City Hall Address"])
    	new_politician.save()