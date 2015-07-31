# -*- coding: utf-8 -*-

from google.appengine.api import urlfetch
import jinja2
import json
import os
import random
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset = utf-8'

        url = "http://api.openweathermap.org/data/2.5/weather?lat=-33.8650&lon=151.2094"
        fetch_weather = urlfetch.fetch(url)
        
        if fetch_weather.status_code == 200:
            weather_dict = json.loads(fetch_weather.content)
            city = weather_dict["name"]
            temp = weather_dict["main"]["temp"] - 273.15
            condition = weather_dict["weather"][0]["main"]
        
        puppy = [{'img': "img/sleepy-pup.jpg", 
                  'url': "https://www.flickr.com/photos/hand-nor-glove/378065479/", 
                  'licence': "hand-nor-glove CC BY-NC_ND 2.0"}, 
                 {'img': "img/rain-pup.jpg",
                  'url': "https://www.flickr.com/photos/alleykitten/3250509977/",
                  'licence': "alleykitten CC BY-NC-ND 2.0"},
                 {'img': "img/snow-pup.jpg",
                  'url': "https://www.flickr.com/photos/aukirk/16623977151/",
                  'licence': "aukirk CC BY 2.0"}]

        template_values = {
            'city': city,
            'temp': temp,
            'condition': condition,
            'puppy': random.choice(puppy)
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


app = webapp2. WSGIApplication([
    ('/', MainPage),
], debug = True)
