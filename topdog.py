# -*- coding: utf-8 -*-

import cgi
from google.appengine.api import urlfetch
import jinja2
import json
import os
import urllib
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


PUPPIES = [{'img': "img/rain-pup.jpg",
            'url': "https://www.flickr.com/photos/smalleraperture/3007432892/",
            'licence': "Eric Osmundson CC BY-NC-SA 2.0",
            'weather': "rain"},
           {'img': "img/snow-pup.jpg",
            'url': "https://www.flickr.com/photos/aukirk/16623977151/",
            'licence': "Austin Kirk CC BY 2.0",
            'weather': "snow"},
           {'img': "img/mist-pup.jpg",
            'url': "https://www.flickr.com/photos/sonstroem/38762487242/",
            'licence': "Eric Sonstroem CC BY 2.0",
            'weather': "mist"},
           {'img': "img/clear-pup.jpg",
            'url': "https://www.flickr.com/photos/31867959@N04/15130078190/",
            'licence': "Dallas Krentzel CC BY 2.0",
            'weather': "clear"},
            {'img': "img/cloud-pup.jpg",
            'url': "https://www.flickr.com/photos/ronk-foto/37235466596/",
            'licence': "Ron Kretschmann CC BY-NC-SA 2.0",
            'weather': "cloud"}]


class MainPage(webapp2.RequestHandler):

    def get(self):
        response = get_url('Sydney')
        self.response.write(response)

    def post(self):
        response = get_url(self.request.get('place').replace(" ", ""))
        self.response.write(response)


def get_url(place):
    # remove white space in input city
    field = {"q": cgi.escape(place)}
    city = urllib.urlencode(field)
    url = "http://api.openweathermap.org/data/2.5/weather?" + city + \
        "&APPID=cf62fd8aa01dd3ebeada9cdec7ff6f8a"

    weather_response = urlfetch.fetch(url)

    if weather_response.status_code != 200:
        template = JINJA_ENVIRONMENT.get_template('error.html')
        return template.render(
            {'error': weather_response.status_code})
    else:
        template_values = get_weather(weather_response.content)
        template = JINJA_ENVIRONMENT.get_template('index.html')
        return template.render(template_values)


def get_weather(weather_response_content):
    weather_dict = json.loads(weather_response_content)
    city = weather_dict["name"]
    country = weather_dict["sys"]["country"]
    temp = round(weather_dict["main"]["temp"] - 273.15, 1)
    condition = weather_dict["weather"][0]["description"]

    displayed_puppy = get_puppy(condition)

    weather_values = {
        'city': city,
        'country': country,
        'temp': temp,
        'condition': condition,
        'puppy': displayed_puppy
    }
    return weather_values


def get_puppy(condition):
    displayed_puppy = PUPPIES[0]
    for puppy in PUPPIES:
        if puppy['weather'] in condition.lower(): #condition.lower():
            displayed_puppy = puppy
    return displayed_puppy


app = webapp2. WSGIApplication([
    ('/', MainPage),
], debug=True)
