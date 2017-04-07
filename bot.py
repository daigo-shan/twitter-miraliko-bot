# -*- coding: utf-8 -*-
 
import tweepy
import twiauth
import random
import datetime
import gacha as gc
import weathermap as wm

NOW = 0  # 今日
TOMORROW = 1 # 明日
DAY_AFTER_TOMORROW = 2 # 明後日

LAST_ONAIR = datetime.date(2017,1,29) # まほプリ公式最終回放送日


#認証とインスタンス生成
api = tweepy.API(twiauth.oauth())

class myException(Exception): pass
        
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        status_id = status.id  # 取得ツイートのID
        screen_name = status.author.screen_name.encode("UTF-8") # 取得ツイートのツイート主
        reply_text="@" + screen_name

        # 時報アカウントのツイートを取得したら時刻をツイートする
        if screen_name == 'k0_0t':
            today = datetime.datetime.today()
            jikoku = today.strftime("%Y/%m/%d %H:%M")
            tweet_text = jikoku + " 稼働中\n現在の機能が知りたい時は「機能」とリプライしてください"
            api.update_status(status=tweet_text)

        # リプライを受け取った場合
        if status.in_reply_to_screen_name == 'MiraLiko_bot':

            # 天気を返す場合
            get_weather(status.text, reply_text, status_id)
            # 怒る場合
            angry(status.text, reply_text, status_id)
            # 機能を返す場合
            func_tweet(status.text, reply_text, status_id)
            
        # TL上に[みらリコガチャ]の文字列を見つけた場合
        if(u'みらリコガチャ' in status.text and screen_name != 'MiraLiko_bot'):

            pic = gc.get_miraliko()

            reply_text += " No." + pic[0] + " " + pic[1]
            api.update_status(status=reply_text,in_reply_to_status_id=status_id)

        # TL上に[今週のまほプリ]の文字列を見つけた場合
        if(u'今週のまほプリ' in status.text and screen_name != 'MiraLiko_bot'):
            reply_text += thisweek_onair()
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


def thisweek_onair():
    # 最終回放送日と現在の日付から何週経過したのか計算
    # 現在話数と現在曜日の特定
    today = datetime.date.today()
    sub = today - LAST_ONAIR
    onair_num = sub.days / 7 + 50
    # 曜日は日付の差分を7で割った余りを使用(日～土:0～6)
    youbi = sub.days % 7
    # 0の時は"今日"
    if(youbi == 0):
        text = "\n今週の魔法つかいプリキュア！は第{n}話で、今日の8:30より放送開始です。" \
            .format(n=onair_num)
    else:
        sub_youbi= 7 - youbi
        next_onair = today + datetime.timedelta(days=sub_youbi)
        text = "\n今週の魔法つかいプリキュア！は第{n}話でした。次回の放送は{d} 8:30からです。" \
               .format(n=onair_num,d=next_onair)

    return text
        


# 機能をお知らせする
def func_tweet(tweet, reply, id):
    if (u'機能' in tweet):
        reply += " [現在の機能]\n" + \
                 "・みらリコガチャ(第3話まで)\n " + \
                 "・今週のまほプリ(←の単語に反応して現在話数をお知らせ)\n" + \
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
