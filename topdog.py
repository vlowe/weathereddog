# -*- coding: utf-8 -*-

import webapp2
import random

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset = utf-8'
        temp = random.randrange(5, 40)
        self.response.write(
            '<h1>Sydney\'s weather ' + str(temp) + '°C</h1>'
            '<img src="img/sleepy-pup.jpg">'
            '''<a href="https://www.flickr.com/photos/hand-nor-glove/378065479/">
                 hand-nor-glove CC BY-NC-ND 2.0
               </a>''')

app = webapp2. WSGIApplication([
    ('/', MainPage),
], debug = True)
