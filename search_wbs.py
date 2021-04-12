#import psaw
from psaw import PushshiftAPI
import datetime

api = PushshiftAPI()
#copied from PSAW website
#this basically collects info from posts made on 3/1/21 in Wallstreetbets subreddit and 
#sorts all obtained info into a list called submissions.
start_time = int(datetime.datetime(2021, 3, 1).timestamp())

submissions = api.search_submissions(after=start_time,
                                     subreddit='wallstreetbets',
                                     filter=['url','author', 'title', 'subreddit'],
                                     limit = 900)
#------------------------------------------------------------------------------------------
for i in submissions:
    #print(" test ")
    #print(i)
    #print(i.created_utc)
    #print(i.title)
    #print(i.url)

    
    words = i.title.split()     #print out all words in title of posts with each word spaced
    stock = list(set(filter(lambda word: word.lower().startswith('$'), words)))     #filter down words in list to match those starting with '$'

    if len(stock) > 0:  #make sure list is not empty
        print(i.title)
        print(stock)    #print list