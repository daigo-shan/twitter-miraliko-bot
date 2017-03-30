# -*- coding: utf-8 -*-
 
import tweepy
import twiauth
import random
import datetime
import gacha as gc
import weathermap as wm

NOW = 0
TOMORROW = 1
DAY_AFTER_TOMORROW = 2

#認証とインスタンス生成
api = tweepy.API(twiauth.oauth())

#時刻用

class myException(Exception): pass

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        
        status_id = status.id
        screen_name = status.author.screen_name.encode("UTF-8")
        reply_text="@" + screen_name

        #時報アカウントのツイートを取得したら時刻をツイートする
        if screen_name == 'jiho_oshirase':
            today = datetime.datetime.today()
            jikoku = today.strftime("%Y/%m/%d %H:%M")
            tweet_text = jikoku + " 稼働中\n現在の機能が知りたい時は「機能」とリプライしてください"
            api.update_status(status=tweet_text)

        #リプライを受け取った場合
        if status.in_reply_to_screen_name == 'MiraLiko_bot':

            #天気を返す場合
            get_weather(status.text, reply_text, status_id)
            #怒る場合
            angry(status.text, reply_text, status_id)
            #機能を返す場合
            func_tweet(status.text, reply_text, status_id)
            
        #TL上に[みらリコガチャ]の文字列を見つけた場合
        if(u'みらリコガチャ' in status.text):

            pic = gc.get_miraliko()

            reply_text += " No." + pic[0] + " " + pic[1]
            api.update_status(status=reply_text,in_reply_to_status_id=status_id)

        return True

       
    def on_timeout(self):
        print('Timeout...')
        raise myException

    def on_error(self, status_code):
        print "error code "
        print status_code
        raise myException
        

#天気を返す関数
#tweet:自分宛のリプライ
#reply:相手への返信用文字列(初期値には相手のID)
#id:返信先ツイートのID
def get_weather(tweet, reply, id):
    if (u'今の天気' in tweet):
        reply += wm.get_weather(NOW)
        api.update_status(status=reply,in_reply_to_status_id=id)
    elif (u'明日の天気' in tweet):
        reply += wm.get_weather(TOMORROW)
        api.update_status(status=reply,in_reply_to_status_id=id)
    elif (u'明後日の天気' in tweet):
        reply += wm.get_weather(DAY_AFTER_TOMORROW)
        api.update_status(status=reply,in_reply_to_status_id=id)
    #上記以外のリプなら何もしない
    else:
        return True

#怒る関数
def angry(tweet, reply, id):
    
    if (u'みらりこ' in tweet):
        reply += " み　ら　リ　コだっつってんだろ(マジギレ)" + \
                 "(オタク特有の早口)(ﾍﾟﾁｬｸﾁｬ)(まほプリのラバスト)" + \
                 "(まほプリの缶バッジ)(キュアップ・ラパパ)"
        api.update_status(status=reply,in_reply_to_status_id=id)

    elif (u'朝比奈みらい' in tweet):
        reply += "\n朝　日　奈　み　ら　い\nだ\nにどとまちがえるなくそが"
        api.update_status(status=reply,in_reply_to_status_id=id)
    else:
        return True


# 機能をお知らせする
def func_tweet(tweet, reply, id):
    if (u'機能' in tweet):
        reply += " 現在の機能\n" + \
                 "・ガチャ(第3話まで)\n " + \
                 "・天気予報(「今/明日/明後日の天気」とリプライ)\n" + \
                 "・「みらりこ」「朝比奈みらい」とリプライするとキレる"
        
        api.update_status(status=reply,in_reply_to_status_id=id)
    else:
        return True
        
if __name__ == '__main__':
    listener = StreamListener()
    auth = api.auth
    stream = tweepy.Stream(auth,listener)
    stream.timeout = None

    while True:
        
        try:
            print "[TL取得開始]"
            stream.userstream()

        except KeyboardInterrupt:
            print("[終了します]")
            exit()

        except:
            print "[再接続]"
            stream = tweepy.Stream(auth, listener)
            stream.timeout = None
