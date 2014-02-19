
import os
import cgi
import hmac
import random
import string
import jinja2
import webapp2
import datetime
import re
import json
import logging

from google.appengine.api import mail


from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.api import users



template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=True, variable_start_string='{{{', variable_end_string='}}}')



class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a,**kw)

    def render_str(self, template, params):
        t = jinja_environment.get_template(template)

        return t.render(params)

    def render(self, template, kw):
        self.write(self.render_str(template, kw))



    # Name - set_cookie
    # Desc
    #   Sets a cookie given the name and value
    # params
    #   self  : Ref    -> reference to object instance
    #   _args : object :: name       : String  -> name of cookie
    #                  :: value      : String  -> contents of cookie
    #                  :: [validity] : Integer -> validity period of cookie default=4wks
    # returns
    #   : Void -> returns nothing

    def set_cookie(self, _args):
        self.response.headers.add_header('Set-Cookie', '%s=%s|%s; expires=%s' %
             (str(_args["name"]), str(_args["value"]), self.Hash_string(_args["value"]),
              (datetime.datetime.now()
              + datetime.timedelta(weeks=_args["validity"] | 4)).strftime('%a, %d %b %Y %H:%M:%S GMT')))



    # Name - get_cookie
    # Desc
    #   retrieves the value of a given cookie
    # params
    #   self        : Ref    -> reference to object instance
    #   name  : String -> name of cookie to be retrieved
    # returns
    #   : List -> list containing a plain text cookie and it's hash or [None, None] if not found

    def get_cookie(self, name):
        cookie = self.request.cookies.get(name, None)

        if cookie:
            temp = cookie.split('|')
            return temp
        else:
            return [None, None]


    # Name - delete_cookie
    # Desc
    #   deletes a given cookie given the name
    # params
    #   self        : Ref    -> reference to object instance
    #   name  : String -> name of cookie to be deleted
    # returns
    #   : Void
    def delete_cookie(self, name):
        self.response.delete_cookie(name)


