from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt


def percentage(part, whole):
    temp = 100 * float(part) / float(whole)
    return format(temp, '.2f')

consumerKey='yAXlgXMqCtKLRiesMxExI9S36'
consumerSecret='4Plwv4Eqchk3j2GmXS8h08sVa4nPkfODhGfngA4KZbEs4k7r6i'
accessToken='1234903159283126272-yt7ah1dfODB0Wx9q1nnf5cApgVggLy'
accessTokenSecret='kv2pHHXShpabzyTwkyXPdIIIVgUGMUgeQfDIPuVvNRpz1'


auth=tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api=tweepy.API(auth)


searchTerm=input("enter keyword to search about:")
noOftweets=int(input("enter no of tweets to analyze:"))

tweets=tweepy.Cursor(api.search,q=searchTerm,lang="en").items(noOftweets)

positive=0
negative=0
neutral=0
polarity=0
i=0
for tweet in tweets:
    #print(i)
    print("::::::::",tweet.text)
    analysis=TextBlob(tweet.text)
    polarity +=analysis.sentiment.polarity
    i+=1

    if (analysis.sentiment.polarity == 0.00):
        neutral +=1
    elif (analysis.sentiment.polarity > 0.00):
        positive +=1
    elif (analysis.sentiment.polarity < 0.00):
        negative +=1


positive=percentage(positive,noOftweets)
negative=percentage(negative,noOftweets)
neutral=percentage(neutral,noOftweets)
polarity=percentage(polarity,noOftweets)
polarity=float(polarity)
print(polarity)


print("Analysis On "+searchTerm+" on "+str(noOftweets)+"number of Tweets")
if (polarity == 0.00):
    print("Neutral")
elif (polarity > 0.00):
    print("Positive")
else:
    print("Negative")



labesl=['Positive['+str(positive)+'%]','Neutral['+str(neutral)+'%]','Negative['+str(negative)+'%]']
size=[positive,neutral,negative]
colors=['green','blue','red']
patches,texts=plt.pie(size,colors=colors,startangle=90)
plt.legend(patches,labesl,loc="best")
plt.title("Analysis On "+searchTerm+" on "+str(noOftweets)+" number of Tweets")
plt.axis('equal')
plt.tight_layout
plt.show()