
from requests_oauthlib import OAuth1Session
import secrets
import json

client_key = secrets.client_key
client_secret = secrets.client_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)

res = json.loads(r.text)
res_list = res['statuses']
for i in res_list:
    auth = i['entities']['user_mentions']
    if auth != []:
        print(auth[0]['screen_name']+":")
    print(i['text'])
    print("-"*9)
