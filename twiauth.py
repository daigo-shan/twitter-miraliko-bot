import tweepy

def oauth():
    consumer_key = '8esCI1ZaJFZScU1nyVFdol7Mj'
    consumer_secret = 'OxuCVTOMAj8SdhJlGM9VgHMxtUEqkB3PezPIQztvgs1BszYqPI'
    access_token = '3023364853-lKIJVfSMqmaArxZuHcxBNxnpzmNbvKYK6h6uNT5'
    access_token_secret = 'baeR11iQb2oh7qD1ByQF7sjjd64hu14WsXuKAN1HZraps'
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth
