# -*- coding: utf-8 -*-
import urllib2, sys
import json

try: citycode = sys.argv[1]
except: citycode = '070030' #若松
resp = urllib2.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()

resp = json.loads(resp)

def return_json():
    return resp


#today = resp['forecasts'][0]['dateLabel']
#weather_today = resp['forecasts'][0]['telop']
#maxtemp_today = resp['forecasts'][0]['temperature']['max']['celsius']
#mintemp_today = resp['forecasts'][0]['temperature']['min']['celsius']

#tomorrow = resp['forecasts'][1]['dateLabel']
#weather_tomo = resp['forecasts'][1]['telop']

#maxtemp_tomo = resp['forecasts'][1]['temperature']['max']['celsius']
#mintemp_tomo = resp['forecasts'][1]['temperature']['min']['celsius']

#after2d = resp['forecasts'][2]['dateLabel']
#weather_a2d = resp['forecasts'][2]['telop']
#maxtemp_a2d = resp['forecasts'][2]['temperature']['max']['celsius']
#mintemp_a2d = resp['forecasts'][2]['temperature']['min']['celsius']
