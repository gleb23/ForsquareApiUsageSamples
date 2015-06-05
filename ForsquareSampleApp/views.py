import string
from django.shortcuts import render_to_response
from pyjavaproperties import Properties
import urllib2
import json

import logging

# Get an instance of a logger
from ForsquareSampleApp.response_parser import parse_checkins, parse_places

logger = logging.getLogger(__name__)

p = Properties()
p.load(open('app.properties'))
client_id = p['client.id']
client_secret = p['client.secret']
redirect_uri = p['redirect.uri']

access_token = None

def access_page(request):
    return render_to_response("access_page.html", {'redirect_uri': redirect_uri,
                                                   'client_id': client_id})


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
                             'DATE': '20150421'})).read()
    return render_to_response('check-ins.html', {'checkins': parse_checkins(json.loads(response))})


def coordinates_to_comma_separated_string(coordinates):
    pass


def all_places(request):
    #coordinates = request.GET['coordinates']
    #response = urllib2.urlopen(string.Template('https://api.foursquare.com/v2/venues/search?ll=$COMMA_SEPARATED_COORDINATES&oauth_token=BLELVGEJOZ5P0HPVMH24RJ4CP1GRZ1I5DTMYAVQLYR0EYBEU&v=$DATE')
    response = urllib2.urlopen(string.Template('https://api.foursquare.com/v2/venues/search?near=Kyiv&oauth_token=BLELVGEJOZ5P0HPVMH24RJ4CP1GRZ1I5DTMYAVQLYR0EYBEU&v=$DATE')
                .substitute({
                            #'COMMA_SEPARATED_COORDINATES': coordinates,
                            'ACCESS_TOKEN': access_token,
                             'DATE': '20150604'})).read()
    return render_to_response('places.html', {'places': parse_places(json.loads(response))})

# def notifications(request):
#     response = urllib2.urlopen(string.Template('https://api.foursquare.com/v2/checkins/recent?oauth_token=$ACCESS_TOKEN&v=$DATE')
#                 .substitute({'ACCESS_TOKEN': access_token,
#                              'DATE': '20150421'})).read()
#     return render_to_response('check-ins.html', {'places': parse_checkins(json.loads(response))})
