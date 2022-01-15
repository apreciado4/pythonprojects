"""
This program downloads a json that returns a list of people currently in the
International Space Station and prints
"""
import json
import datetime
import time
import turtle
import urllib.request

sflat = 37.710227966308594
sflong= -122.43498992919922

image = 'map.gif'

peopleurl ="http://api.open-notify.org/astros.json"
gpsurl = "http://api.open-notify.org/iss-now.json"
passoverurl ="http://api.open-notify.org/iss-pass.json"
passoverurl = passoverurl + '?lat=' + str(sflat) + '&lon=' + str(sflong)


def getdata(url):
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    return result

peopledata = getdata(peopleurl)
print("There are", peopledata['number'], "people in space")
people = peopledata['people']
for p in people:
    print('{name} is aboard the {craft}'.format(
                name = p['name'],
                craft =p['craft']))

gpsdata = getdata(gpsurl)
timestamp = datetime.datetime.fromtimestamp(gpsdata['timestamp'])
position = gpsdata['iss_position']
longitude = float(position['longitude'])
latitude = float(position['latitude'])
print('\nAt {}'.format(timestamp))
print('The ISS was at latitude {lat}, and longitude {long}'.format(
                lat = latitude,
                long = longitude))

passoverdata = getdata(passoverurl)
passover = passoverdata['response'][1]['risetime']
# print(time.ctime(passover))

screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic(image)

location = turtle.Turtle()
location.penup()
location.color('orange')
location.goto(sflong, sflat)
location.dot(10)
location.hideturtle()

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
iss.penup()
iss.goto(longitude, latitude)

style = ('arial', 6, 'bold')
location.write(time.ctime(passover), font='style')

turtle.done()
