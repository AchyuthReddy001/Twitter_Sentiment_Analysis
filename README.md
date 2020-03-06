# Twitter_Sentiment_Analysis
Dependency Required:::tweepy and textblob







Install:pip install tweepy,textblod


textblob:python lib that used to preproceesing on text and it is a NLP technique

from textblob import TextBlob

text=TextBlob("I am a good programmer")

text.tags

output:('I','prp'),('good','JJ').....so on

text.words

output;(['I','am','good','programmer']

text.polarity

output:+1

text2=TextBlob("I am a bad programmer")

text.polarity

output:-1
