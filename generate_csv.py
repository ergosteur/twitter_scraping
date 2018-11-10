import tweepy
import json
import math
import glob
import csv
import zipfile
import zlib
from tweepy import TweepError
from time import sleep
user = 'gibiofficial'
user = user.lower()
with open('gibiofficial_short.json') as master_file:
    data = json.load(master_file)
    fields = ["favorite_count", "source", "text", "in_reply_to_screen_name", "is_retweet", "created_at", "retweet_count", "id_str"]
    print('creating CSV version of minimized json master file')
    f = csv.writer(open('gibiofficial2.csv', 'w', quotechar='"', encoding='utf-8'))
    f.writerow(fields)
    for x in data:
        f.writerow([x["favorite_count"], x["source"], x["text"], x["in_reply_to_screen_name"], x["is_retweet"], x["created_at"], x["retweet_count"], x["id_str"]])