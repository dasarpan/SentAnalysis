# Example to do sentiment analysis on tweets

import twitter
import json
import numpy as np
import nltk     # Natural Language Toolkit
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
import pandas as pd
# Imported to create word clouds 
from wordcloud import WordCloud
import matplotlib.pyplot as plt


analyzer = SentimentIntensityAnalyzer()




def sentimentanalysis(filename):
  data = pd.read_csv(filename, encoding='ISO-8859-1')
  df = pd.DataFrame(data['text'])
  df.columns = ['text']
  df = df.dropna()

  scores = np.zeros(len(df['text']))
  pos_scores = np.zeros(len(df['text']))
  neu_scores = np.zeros(len(df['text']))
  neg_scores = np.zeros(len(df['text']))

  for i, t in enumerate(df['text']):
    # Extract the text portion of the tweet
    #text = t['text']
    
    # Measure the polarity of the tweet
    polarity = analyzer.polarity_scores(t)
    if(polarity['pos'] > 0 or polarity['neg'] > 0):
      # Store the normalized, weighted composite score
      scores[i] = polarity['compound']
      pos_scores[i] = polarity['pos']
      neu_scores[i] = polarity['neu']
      neg_scores[i] = polarity['neg']


  scoresdf1 = pd.DataFrame(pos_scores)
  scoresdf2 = pd.DataFrame(neu_scores)
  scoresdf3 = pd.DataFrame(neg_scores)
  scoresdf4 = pd.DataFrame(scores)

  scoresdf1.columns = ['pos_scores']
  scoresdf2.columns = ['neu_scores']
  scoresdf3.columns = ['neg_scores']
  scoresdf4.columns = ['compound']

  df = pd.concat([df, scoresdf1, scoresdf2, scoresdf3, scoresdf4], axis=1)
  print(df.info())


  str_sentiment = ''.join(list(df['text']))
  wordcloud_mining = WordCloud().generate(str_sentiment)
  plt.figure(figsize = (15,8)) 
  plt.axis('off') 
  plt.imshow(wordcloud_mining,interpolation='bilinear')
  #plt.show()

  #most_positive = np.argmax(scores)
  #most_negative = np.argmin(scores)

  #print(df['text'].iloc[most_positive], '\n')
  #print(df['text'].iloc[most_negative])

  posavg = np.average(df['pos_scores'])
  neuavg = np.average(df['neu_scores'])
  negavg = np.average(df['neg_scores'])
  compavg = np.average(df['compound'])

  print("VADER Analysis Average Positive Score:", posavg)
  print("VADER Analysis Average Neutral Score:", neuavg)
  print("VADER Analysis Average Negative Score:", negavg)
  print("VADER Analysis Average Compound Score:", compavg)


sentimentanalysis('tweetsSeattle.csv')
sentimentanalysis('tweetsSeattle2.csv')