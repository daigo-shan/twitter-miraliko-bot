# -*- coding: utf-8 -*-
 
import tweepy

consumer_key = 'bTeYw5k6BPRfHsJOPeThEVDZe'
consumer_secret = '78lUgkrKqL0FEvxd5RXNFl1IXvnPEapMbIKSU1eb4BajY3RV6X'
access_token = '834972905624608768-qHHU4j0fhIS7M3fIBYeZtGCVDpvlowt'
access_token_secret = 'Qu1EMLFNTKv79lwjlBdtbHhCbGPz0iOhY6SvmEogdaJhO'
    
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text

        f = open( "pic_url.txt", "a" )
        try:
            # 文字列を出力
            f.write(status.text)
            f.write('\n')
        finally:
            f.close()

    def on_timeout(self):
        print('Timeout...')
        return True

    def on_error(self, status_code):
        if status_code == 420:
            print str(status_code)
            return False
        
if __name__ == '__main__':
    try:
        stream = tweepy.Stream(auth=api.auth, listener=StreamListener())
        stream.userstream()
        
    except KeyboardInterrupt:
        print("終了します")
        exit()
    
