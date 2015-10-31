# -*- coding: utf-8 -*-

import os,sys,time,datetime
import urllib

try:
  import dateutil.parser
except:
  sys.exit ( 'Error: dateutils module not installed' )

from urlparse import urlparse
 
from google.appengine.api import users, urlfetch
from google.appengine.ext import ndb
from flask import Flask, request, Response

from flaskext.appengine import(
  AppEngine, login_required
)

from acctrl.access import(
 whitelist_checked  
)


import jinja2
jn2 = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

gae = AppEngine(app)

from target.general import *
from target.alert import *
from target.weather import *
from target.trunko import *
from target.yahoorss import *

class whitelist(ndb.Model):
  host = ndb.StringProperty(required=True)
  pause = ndb.StringProperty(required=True, choices=set( ['false','true'] ) )

  @classmethod
  def query_host(cls, key):
    return cls.query()




