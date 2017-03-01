# -*- coding: utf-8 -*-
 
import tweepy
import twiauth
import random
import time
import gacha as gc
import weather_bot as wb

#認証とインスタンス生成
api = tweepy.API(twiauth.oauth())

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        status_id = status.id
        screen_name = status.author.screen_name.encode("UTF-8")
        reply_text="@" + screen_name

        #リプライを受け取った場合
        if status.in_reply_to_screen_name == 'MiraLiko_bot':

            #天気を返す場合
            get_weather(status.text, reply_text, status_id)
            #怒る場合
            angry(status.text, reply_text, status_id)
            
        #TL上に[みらリコガチャ]の文字列を見つけた場合
        if(u'みらリコガチャ' in status.text):

            pic = gc.get_miraliko()

            reply_text += " No." + str(pic[0]) + " " + pic[1]
            api.update_status(status=reply_text,in_reply_to_status_id=status_id)

       
    def on_timeout(self):
        print('Timeout...')
        return True

    def on_error(self, status_code):
        if status_code == 420:
            print str(status_code)
            return False

#天気を返す関数
def get_weather(tweet, reply, id):
    if (u'今日の天気' in tweet):
        weather = wb.weather_text(0)
        reply += weather
        api.update_status(status=reply,in_reply_to_status_id=id)
    elif (u'明日の天気' in tweet):
        weather = wb.weather_text(1)
        reply += weather
        api.update_status(status=reply,in_reply_to_status_id=id)
    elif (u'明後日の天気' in tweet):
        weather = wb.weather_text(2)
        reply += weather
        api.update_status(status=reply,in_reply_to_status_id=id)
    else:
        return True

#怒る関数
def angry(tweet, reply, id):
    
    if (u'みらりこ' in tweet):
        reply += " み　ら　リ　コだっつってんだろ(マジギレ)(オタク特有の早口)(ﾍﾟﾁｬｸﾁｬ)(まほプリのラバスト)(まほプリの缶バッジ)(キュアップ・ラパパ)"
        api.update_status(status=reply,in_reply_to_status_id=id)
    else:
        return 0
        
if __name__ == '__main__':
    try:
        stream = tweepy.Stream(auth=api.auth, listener=StreamListener())
        stream.userstream()

    except KeyboardInterrupt:
        print("終了します")
        exit()
