# -*- coding: utf-8 -*-

import urllib2
import json
import pprint
import math

#キャラクター切り替え用変数
chara = 0
MIRAI = 0
LIKO = 1
#日にちリスト
day_list = ['今','明日','明後日']

location = "Ōdera,jp"   #おおでら？会津付近(らしい)
mode = "json"           #json形式で取得
metric = "metric"       #セ氏形式
key = "fc183fae5bf909e94699a5efa47606eb"

#現在天気取得用
url1 = "http://api.openweathermap.org/data/2.5/weather?q={a}&mode={b}&units={c}&appid={d}".format(a=location, b=mode, c=metric, d=key)
#明日,明後日の天気取得用
url2 = "http://api.openweathermap.org/data/2.5/forecast/daily?q={a}&mode={b}&units={c}&cnt=3&appid={d}".format(a=location, b=mode, c=metric, d=key)


#取得した天気を日本語に変換する関数
#晴れ,雪ならキャラをみらいに変更
#曇り,雨ならキャラをリコに変更
def text_convert(tenki):

    if(tenki == 'Clear'):
        tenki = '晴れ'
        chara = MIRAI
    if(tenki == 'Clouds'):
        tenki = '曇り'
        chara = LIKO
    if(tenki == 'Rain'):
        tenki = '雨'
        chara = LIKO
    if(tenki == 'Snow'):
        tenki = '雪'
        chara = MIRAI
    return tenki

#晴れ,雪ならみらい口調で返す関数
def mirai_mode(day,tenki,humidity,temp):
    #今の天気の場合
    if(day == '今'):
        text = "\n今の天気は{w}だよ！\n気温は{t}℃で、湿度は{h}%だね。".format(w=tenki,t=temp[0],h=humidity)
    #明日明後日の場合
    else:
        text = "\n{d}の天気は{w}の予報だよ〜！\n最高気温は{max}℃、最低気温は{min}℃みたいだね。".format(d=day,w=tenki,max=temp[0],min=temp[1])
    return(text)

    
#雨,曇りならリコ口調で返す関数
def liko_mode(day,tenki,humidity,temp):
    #今の天気の場合
    if(day == '今'):
        text = "\n今の天気は{w}ね。\n気温は{t}℃で、湿度は{h}%よ。".format(w=tenki,t=temp[0],h=humidity)
    else:
        text = "\n{d}の天気は{w}の予報よ。\n最高気温は{max}℃、最低気温は{min}℃みたいね。".format(d=day,w=tenki,max=temp[0],min=temp[1])
    return(text)



#天気情報を取得する関数
#day:0~2の定数.[今,明日,明後日]
def get_weather(day):

    #今の天気の場合
    if(day == 0):
        #天気情報の取得
        response = urllib2.urlopen(url1)
        weather = json.loads(response.readline())
    
        #天気を取得し日本語変換
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

        if(chara == MIRAI):
            text = mirai_mode(day_list[day],tenki,humidity,temp)
        elif(chara == LIKO):
            text = liko_mode(day_list[day],tenki,humidity,temp)

        return(text)

    else: #明日明後日の場合
        response = urllib2.urlopen(url2)
        weather = json.loads(response.readline())
        tenki = weather['list'][day]['weather'][0]['main']
        tenki = text_convert(tenki)
        humidity = ' '
        #temp = [最高気温,最低気温]
        temp = []
        max = round(weather['list'][day]['temp']['max'])
        min = round(weather['list'][day]['temp']['min'])
        if(max == -0.0):
            max = 0.0
        if(min == -0.0):
            min = 0.0
        temp.insert(0,max)
        temp.insert(1,min)
    
        if(chara == MIRAI):
            text = mirai_mode(day_list[day],tenki,humidity,temp)
        elif(chara == LIKO):
            text = liko_mode(day_list[day],tenki,humidity,temp)

        return(text)

#不快指数
def DiscomfortIndex(T,H):
    di = 0.81*T+0.01*H*(0.99*T-14.3)+46.3
    return di

if __name__ == '__main__':
    get_weather(0)
    get_weather(1)
    get_weather(2)
