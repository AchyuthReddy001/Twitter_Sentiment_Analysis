from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler

consumerKey='use your consumerkey'
consumerSecret='use your consumerSecret'
accessToken='use your consumer access Token'
accessTokenSecret='use your consumer access Token secret'

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


