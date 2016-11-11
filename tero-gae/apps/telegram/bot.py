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
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'


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


@telegram.route('/reset-webhook')
def reset_webhook():
    urlfetch.set_default_fetch_deadline(60)
    url = "" 
    api_url = BASE_URL + 'setWebhook?url=' + url
    return json.dumps(json.load(urllib2.urlopen(api_url)))


@telegram.route('/set-webhook')
def set_webhook():
    urlfetch.set_default_fetch_deadline(60)
    url = request.args.get('url') 
    api_url = BASE_URL + 'setWebhook?url=' + url
    return json.dumps(json.load(urllib2.urlopen(api_url)))


@telegram.route('/webhook-info')
def webhook_info():
    urlfetch.set_default_fetch_deadline(60)
    api_url = BASE_URL + 'setWebhook'
    return json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getWebhookInfo')))


@telegram.route('/webhook', methods=['POST'])
def webhook():
    urlfetch.set_default_fetch_deadline(60)
    data = request.get_json()
    message = data['message']
    from_id = message['from']['id']
    text = message['text']
    message_id = message['message_id']
    chat_id = message['chat']['id']
    msg = 'frulaaaaaaaaaa'
    resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
        'chat_id': str(chat_id),
        'text': msg.encode('utf-8'),
        'disable_web_page_preview': 'true',
        'reply_to_message_id': str(message_id),
    })).read()
    return json.dumps(data)
