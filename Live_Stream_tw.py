from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler

consumerKey='yAXlgXMqCtKLRiesMxExI9S36'
consumerSecret='4Plwv4Eqchk3j2GmXS8h08sVa4nPkfODhGfngA4KZbEs4k7r6i'
accessToken='1234903159283126272-yt7ah1dfODB0Wx9q1nnf5cApgVggLy'
accessTokenSecret='kv2pHHXShpabzyTwkyXPdIIIVgUGMUgeQfDIPuVvNRpz1'

class Stdlis(StreamListener):
    def on_error(self,status):
        print(status)
    def on_data(self,data):
        print(data)



listen=Stdlis()
auth=OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
stream=Stream(auth,listen)
stream.filter(track=['modi','india','caa'])


