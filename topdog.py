# -*- coding: utf-8 -*-

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset = utf-8'
        self.response.write(
            '''<h1>Sydney\'s weather 15°C</h1>
               <img src="img/sleepy-pup.jpg">
               <a href="https://www.flickr.com/photos/hand-nor-glove/378065479/">
                 hand-nor-glove CC BY-NC-ND 2.0
               </a>''')

app = webapp2. WSGIApplication([
    ('/', MainPage),
], debug = True)
