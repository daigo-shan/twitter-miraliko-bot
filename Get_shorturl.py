#coding: utf-8

import tweepy

CK = "CK"
CS = "CS"
AT = "AT"
AS = "AS"

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        s = status.text
        print s
        f = open('picture_list.txt','a')
        f.write(s + "\n")
        f.close()
        

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True


if __name__ == '__main__':
    # Twitterオブジェクトの生成
    
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    listener = Listener()
    stream = tweepy.Stream(auth, listener)
    while True:
            
        try:
            print "[画像取得開始]"
            stream.userstream()
                
        except KeyboardInterrupt:
            print("[終了します]")
            exit()
