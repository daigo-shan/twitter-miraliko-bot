# -*- coding: utf-8 -*-

import weather_api as wp

resp = wp.return_json()
error = u" ごめん、まだわからないや"


def weather_text(flag = 0):
    try:
        day = resp['forecasts'][flag]['dateLabel']
        daytext = "\n" + day + u"の天気は"
        out = daytext 
    except:
        return error
        
        
    telop = resp['forecasts'][flag]['telop']
    teloptext = telop + u"だよ！\n"
    out = out + teloptext

    try:
        maxtemp = resp['forecasts'][flag]['temperature']['max']['celsius']
        maxtext = u"最高気温は" + maxtemp + u"℃！\n"
    except:
        maxtext = u"最高気温は...今は取得できないよ\n"
    try:
        mintemp = resp['forecasts'][flag]['temperature']['min']['celsius']
        mintext = u"最低気温は" + mintemp + u"℃！\n"
    except:
        mintext = u"最低気温は...今は取得できないよ\n"

    out = out + maxtext + mintext

    return out + u"キュアップ・ラパパ！" + day + u"もいい日になーれ！"


if __name__ == '__main__':

   try:
       weather_text(0)
       weather_text(2)
   except:
       print error
