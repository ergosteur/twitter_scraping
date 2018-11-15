import json
import csv

user = 'gibiofficial'
user = user.lower()
with open('data/gibiofficial.json') as master_file:
    data = json.load(master_file)
    fields = ["favorite_count", "source", "full_text", "in_reply_to_screen_name", "is_retweet", "created_at", "retweet_count", "id_str"]
    print('creating CSV version of minimized json master file')
    csvFile = open('data/gibiofficial2.csv'.format(user), 'w', newline='', encoding='utf-8')
    f = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    f.writerow(fields)
    for x in data:
        f.writerow([x["favorite_count"], x["source"], x["text"], x["in_reply_to_screen_name"], x["is_retweet"], x["created_at"], x["retweet_count"], x["id_str"]])