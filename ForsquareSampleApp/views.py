import string
from django.http import HttpResponse
from django.shortcuts import render_to_response
from pyjavaproperties import Properties
import urllib2
import json

import logging

# Get an instance of a logger
from ForsquareSampleApp.response_parser import parse_checkins

logger = logging.getLogger(__name__)

p = Properties()
p.load(open('app.properties'))
client_id = p['client.id']
client_secret = p['client.secret']
redirect_uri = p['redirect.uri']

access_token = None

def access_page(request):
    return render_to_response("access_page.html", {'redirect_uri': redirect_uri,
                                                   'client_id' : client_id})


def parse_code(request):
    code = request.GET['code']

    response = urllib2.urlopen(string.Template('https://foursquare.com/oauth2/access_token?client_id=$CLIENT_ID&client_secret=$CLIENT_SECRET&grant_type=authorization_code&redirect_uri=$REDIRECT_URI&code=$CODE')
                    .substitute({'CLIENT_ID': client_id,
                                 'CLIENT_SECRET': client_secret,
                                 'REDIRECT_URI': redirect_uri,
                                 'CODE': code})).read()
    a = json.loads(response)
    global access_token
    access_token = a['access_token']

    return render_to_response("examples-page.html", {})

def all_check_ins(request):
    response = urllib2.urlopen(string.Template('https://api.foursquare.com/v2/checkins/recent?oauth_token=$ACCESS_TOKEN&v=$DATE')
                .substitute({'ACCESS_TOKEN': access_token,
                             'DATE': '20150420'})).read()
    return HttpResponse(json.dumps(parse_checkins(json.loads(response)), indent=4, sort_keys=True))
