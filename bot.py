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
        
        if status.in_reply_to_screen_name == 'MiraLiko_bot':
            if u'今日の天気' in status.text:
                weather = wb.weather_text(0)
                reply_text += weather
                api.update_status(status=reply_text,in_reply_to_status_id=status_id)
            elif u'明日の天気' in status.text:
                weather = wb.weather_text(1)
                reply_text += weather
                api.update_status(status=reply_text,in_reply_to_status_id=status_id)
            elif u'明後日の天気' in status.text:
                weather = wb.weather_text(2)
                reply_text += weather
                api.update_status(status=reply_text,in_reply_to_status_id=status_id)
                
            
             
        
        if(u'みらリコガチャ' in status.text):

            rare_pic = gc.get_miraliko()

            reply_text += " [" + rare_pic[0] +"] " + rare_pic[1]
            api.update_status(status=reply_text,in_reply_to_status_id=status_id)

        if(u'みらリコ10連ガチャ' in status.text):

            res10 = gc.turn_10rare()

            reply_text += " \n"
            for item in res10:
                reply_text += item + "\n"

            api.update_status(status=reply_text,in_reply_to_status_id=status_id)

        if(u'みらりこ' in status.text):
            reply_text += " み　ら　リ　コだっつってんだろ(マジギレ)(早口)(ﾍﾟﾁｬｸﾁｬ)(めんどくさいオタク)(アディダスの財布)(俊足)(コーナーで差をつけろ)"
            
            api.update_status(status=reply_text,in_reply_to_status_id=status_id)

        if u'49話限定ガチャ' in status.text:
            pic_num = random.randint(1,93)
            filename = '/home/daigo-shan/Pictures/picmaho49/'
            pic_name = 'maho49 (' + str(pic_num) + ').jpg'
            path = filename + pic_name
            api.update_with_media(status = reply_text,filename = path, in_reply_to_status_id = status_id)

           
      
    def on_timeout(self):
        print('Timeout...')
        return True

    def on_error(self, status_code):
        if status_code == 420:
            print str(status_code)
            return False
        
if __name__ == '__main__':
    try:
     #   print(u"[動作開始]")
     #   api.update_status('TL取得開始 ' + time.ctime())
        stream = tweepy.Stream(auth=api.auth, listener=StreamListener())
        stream.userstream()

    except KeyboardInterrupt:
        api.update_status('現在停止中 ' + time.ctime())
        exit()

   # except:
        # 例外が発生したら1分待って接続する
    #    api.update_status('例外発生 ' + time.ctime())
     #   time.sleep(60)
      #  stream = tweepy.Stream(auth=api.auth, listener=StreamListener())
