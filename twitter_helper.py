import twitter
import datetime
import os 


api_key = os.environ.get('TWITTER_API_KEY') 
api_secret = os.environ.get('TWITTER_API_SECRET') 
access_token = os.environ.get('TWITTER_API_TOKEN') 
access_secret = os.environ.get('TWITTER_API_TOKEN_SECRET') 

api = twitter.Api(consumer_key=api_key,consumer_secret=api_secret,access_token_key=access_token,access_token_secret=access_secret)

class tweet:
    def __init__(self, name, text, time):
        self.name = name
        self.text = text
        self.time = time
        
def build_search_text(text, since, count, user):
    # since
    if since == None:
        since = datetime.date.today()
    # count
    if count == None:
        count = "20"
    # text
    if text == None:
        text = "twitter%20"
    # user
    if user == None:
        user = ""
    return f'q={text}&result_type=recent&from={user}&since={since}&count={count}'

def search_twitter(text=None, since=None, count=None, user=None):
    query = build_search_text(text, since, count, user)
    results = api.GetSearch(raw_query=query)
    tweet_list = [tweet(result.user.name, result.text, result.created_at) for result in results]
    return tweet_list


if __name__ == '__main__':

    tweets = search_twitter(text="peta")
    for twt in tweets:
        print(f'{twt.name} ---> {twt.text}')
    