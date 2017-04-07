# -*- coding: utf-8 -*-

import urllib2
import json
import pprint
import random
import math

#キャラクター切り替え用変数
MIRAI = 0
LIKO = 1

#日にちリスト
day_list = ['今','明日','明後日']

location = "Ōdera,jp"   #おおでら？会津付近(らしい)
mode = "json"           #json形式で取得
metric = "metric"       #セ氏形式
key = "fc183fae5bf909e94699a5efa47606eb"

#現在天気取得用
url1 = "http://api.openweathermap.org/data/2.5/weather?q={a}&mode={b}&units={c}&appid={d}"\
    .format(a=location, b=mode, c=metric, d=key)

#明日,明後日の天気取得用
url2 = "http://api.openweathermap.org/data/2.5/forecast/daily?q={a}&mode={b}&units={c}&cnt=3&appid={d}"\
    .format(a=location, b=mode, c=metric, d=key)


#取得した天気を日本語に変換する関数
def text_convert(tenki):
    if(tenki == 'Clear'):
        tenki = '晴れ'
    elif(tenki == 'Clouds'):
        tenki = '曇り'
    elif(tenki == 'Rain'):
        tenki = '雨'
    elif(tenki == 'Snow'):
        tenki = '雪'
    return tenki

def tenki_pic(tenki,chara):
    if(chara == MIRAI):
        if(tenki == '晴れ'):
            pic = "https://t.co/xzOZnCgJIQ"
        elif(tenki == '曇り'):
            pic = "https://t.co/Ep5mt6V8fF"
        elif(tenki == '雨'):
            pic = "https://t.co/ld44zfZoxG"
        elif(tenki == '雪'):
            pic = "https://t.co/HPrdeD5xBx"
    else:
        if(tenki == '晴れ'):
            pic = "https://t.co/BpIlb8IKck"
        elif(tenki == '曇り'):
            pic = "https://t.co/Xf2BDheyYn"
        elif(tenki == '雨'):
            pic = "https://t.co/GEwmoAFy7r"
        elif(tenki == '雪'):
            pic = "https://t.co/kLcMV0Og7I"

    return pic

#みらい口調で返す関数
def mirai_mode(sday,tenki,humidity,temp):
    
    # 天気用の画像URLを取得
    weather_pic = tenki_pic(tenki,MIRAI)
    
    # 今の天気の場合
    if(sday == '今'):
        text = "\n{d}の天気は{w}だよ！\n気温は{t}℃で、湿度は{h}%だね。" \
            .format(d=sday,w=tenki,t=temp[0],h=humidity)
        
    # 明日明後日の場合
    else:
        text = "\n{d}の天気は{w}の予報だよ〜！\n最高気温は{max}℃、最低気温は{min}℃みたいだね。"\
            .format(d=sday,w=tenki,max=temp[0],min=temp[1])

    return text + " " + weather_pic

    
#リコ口調で返す関数
def liko_mode(sday,tenki,humidity,temp):

    # 天気用の画像URLを取得
    weather_pic = tenki_pic(tenki,LIKO)
    
    # 今の天気の場合
    if(sday == '今'):
        text = "\n{d}の天気は{w}ね。\n気温は{t}℃で、湿度は{h}%よ。"\
            .format(d=sday,w=tenki,t=temp[0],h=humidity)

    # 明日明後日の場合
    else:
        text = "\n{d}の天気は{w}の予報よ。\n最高気温は{max}℃、最低気温は{min}℃みたいね。"\
            .format(d=sday,w=tenki,max=temp[0],min=temp[1])

    return text + " " + weather_pic


#天気情報を取得し、ツイート内容を生成する関数
#day:0~2の定数.[今,明日,明後日]
def get_weather(day):

    #今の天気の場合
    if(day == 0):
        # 天気情報の取得
        response = urllib2.urlopen(url1)
        weather = json.loads(response.readline())
    
        # 天気を取得し日本語変換
        tenki = weather['weather'][0]['main']
        tenki = text_convert(tenki)
        
        #湿度
        humidity = weather['main']['humidity']
        
        #現在気温,四捨五入したもの
        temp = []
        nowtemp = round(weather['main']['temp'])
        if(nowtemp == -0.0):
            nowtemp = 0.0
        temp.insert(0,nowtemp)
        temp.insert(1,0.0)

        #口調をランダムで選択
        chara = random.randint(0,1)
        if(chara == MIRAI):
            return mirai_mode(day_list[day],tenki,humidity,temp)
        elif(chara == LIKO):
            return liko_mode(day_list[day],tenki,humidity,temp)


    else: #明日明後日の場合
        response = urllib2.urlopen(url2)
        weather = json.loads(response.readline())
        tenki = weather['list'][day]['weather'][0]['main']
        tenki = text_convert(tenki)
        humidity = ' '
        
        # temp = [最高気温,最低気温]
        temp = []
        max = round(weather['list'][day]['temp']['max'])
        min = round(weather['list'][day]['temp']['min'])
        if(max == -0.0):
            max = 0.0
        if(min == -0.0):
            min = 0.0
        temp.insert(0,max)
        temp.insert(1,min)

        chara = random.randint(0,1)
        if(chara == MIRAI):
            return mirai_mode(day_list[day],tenki,humidity,temp)
        elif(chara == LIKO):
            return liko_mode(day_list[day],tenki,humidity,temp)

        

if __name__ == '__main__':
    print get_weather(0)
    print get_weather(1)
    print get_weather(2)
