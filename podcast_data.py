#from app_store_scraper import Podcast
#from pprint import pprint

#sysk = Podcast(country="nz", app_name="stuff you should know")
#sysk.review(how_many=20)

#pprint(sysk.reviews)
#pprint(sysk.reviews_count)

#var request = require("request");
#var user_id = "david";



#Client ID : 2683c54036bb4c208b41897bdd17b270
#Client Secret : 11699e2c6ad4401fb903527e5a6b9029
#redirect_uri : https%3A%2F%2Fwww.creativityconduit.com%2F
# https://accounts.spotify.com/authorize?client_id=2683c54036bb4c208b41897bdd17b270&response_type=code&redirect_uri=https%3A%2F%2Fwww.creativityconduit.com%2F

import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

cid ="2683c54036bb4c208b41897bdd17b270"
secret = "11699e2c6ad4401fb903527e5a6b9029"

os.environ['SPOTIPY_CLIENT_ID']= cid
os.environ['SPOTIPY_CLIENT_SECRET']= secret
os.environ['SPOTIPY_REDIRECT_URI']='http://localhost:8888/callback'

username = ""
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_top_tracks(limit=50,offset=0,time_range='medium_term')
    for song in range(50):
        list = []
        list.append(results)
        with open('top50_data.json', 'w', encoding='utf-8') as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
    else:
        print("Can't get token for", username)
