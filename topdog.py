# -*- coding: utf-8 -*-

import webapp2
import random

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset = utf-8'
        city = random.choice(['Sydney', 'Melbourne', 'Brisbane', 'Perth',
                              'Adelaide', 'Gold Coast', 'Canberra',
                              'Newcastle', 'Wollongong', 'Logan City'])
        temp = random.randrange(5, 40)
        # http://wiki.wunderground.com/index.php/Educational_-_Partly_cloudy
        condition = random.choice(['Cloudy', 'Clear', 'Mostly Cloudy', 
                                      'Partly Cloudy', 'Partly Sunny', 
                                      'Mostly Sunny', 'Sunny'])

        self.response.write('<title>What\'s the weather, pup?</title>')
        self.response.write(
            '<h1>' + city + '\'s weather is ' + condition + ' and ' + str(temp) + '°C.</h1>'
            '<img src="img/sleepy-pup.jpg"><br>'
            '''<a href="https://www.flickr.com/photos/hand-nor-glove/378065479/">
                 hand-nor-glove CC BY-NC-ND 2.0
               </a>''')

app = webapp2. WSGIApplication([
    ('/', MainPage),
], debug = True)
