# -*- coding: utf-8 -*-

import cgi
from google.appengine.api import urlfetch
import jinja2
import json
import os
import random
import urllib
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)


PUPPIES = [{'img': "img/sleepy-pup.jpg", 
            'url': "https://www.flickr.com/photos/hand-nor-glove/378065479/", 
            'licence': "hand-nor-glove CC BY-NC_ND 2.0"}, 
           {'img': "img/rain-pup.jpg",
            'url': "https://www.flickr.com/photos/alleykitten/3250509977/",
            'licence': "alleykitten CC BY-NC-ND 2.0"},
           {'img': "img/snow-pup.jpg",
            'url': "https://www.flickr.com/photos/aukirk/16623977151/",
            'licence': "aukirk CC BY 2.0"}]

class MainPage(webapp2.RequestHandler):

    def get(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=Sydney"
        template_values = get_weather(url)

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

    def post(self):
        # remove white space in input city
        field = {"q" : cgi.escape(self.request.get('place').replace(" ", ""))}
        city = urllib.urlencode(field)
        url = "http://api.openweathermap.org/data/2.5/weather?" + city

        template_values = get_weather(url)
        fetch_weather = urlfetch.fetch(url)

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


def get_weather(url):
        fetch_weather = urlfetch.fetch(url)

        if fetch_weather.status_code == 200:
            weather_dict = json.loads(fetch_weather.content)
            city = weather_dict["name"]
            country = weather_dict["sys"]["country"]
            temp = weather_dict["main"]["temp"] - 273.15
            condition = weather_dict["weather"][0]["main"]

        template_values = {
            'city': city,
            'country': country,
            'temp': temp,
            'condition': condition,
            'puppy': random.choice(PUPPIES)
        }

        return template_values


app = webapp2. WSGIApplication([
    ('/', MainPage),
], debug = True)
