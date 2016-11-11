import os
import json
import random
import urllib
import logging
import StringIO
import urllib2

from google.appengine.api import urlfetch
from flask import Blueprint, render_template, request
from google.appengine.ext import ndb

TOKEN = '265716638:AAF13GJ7tMGpI4VUTBNzfeG0XiKDXiCLW1Y'
BASE_URL = 'https://api.telegram.org/bot/' + TOKEN + '/'


telegram = Blueprint('telegram', __name__)


def setEnabled(chat_id, yes):
    es = EnableStatus.get_or_insert(str(chat_id))
    es.enabled = yes
    es.put()

def getEnabled(chat_id):
    es = EnableStatus.get_by_id(str(chat_id))
    if es:
        return es.enabled
    return False


@telegram.route('/')
def home():
    return 'blueprint de telegram funcando' 


@telegram.route('/me')
def me():
    urlfetch.set_default_fetch_deadline(60)
    return json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getMe')))


@telegram.route('/get-updates')
def get_updates():
    urlfetch.set_default_fetch_deadline(60)
    return json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getUpdates')))


@telegram.route('/set-webhook')
def set_webhook():
    urlfetch.set_default_fetch_deadline(60)
    url = request.args.get('url') 
    return json.dumps(json.load(urllib2.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url}))))


@telegram.route('/webhook', methods=['POST', 'GET'])
def webhook():
    urlfetch.set_default_fetch_deadline(60)
    if request.method == 'POST':
        return request.get_json()
    return 'la cosa vino por get'
