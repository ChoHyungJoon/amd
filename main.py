import tweepy

# Twitter API credentials
consumer_key = '3N2hyJxUYivUYR0BHblOnOCLF'
consumer_secret = 'dbJZYOaB9sUrDCgbPtWyhfaMpEPXdBwQNTpYt8oOAo2HGz6zvd'
access_token = '1663353232264142849-DjDyMqkB5t4GZ4nEi0rzmQNQz8dWHe'
access_token_secret = 'IJPFrRNqbHTNfNehBLH0Di5vvH4hbHOaaUjtjOfxvsKs2'

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Keyword to search
keyword = 'your_keyword'

# Date range to search within
start_date = '2023-06-01'
end_date = '2023-06-20'

# Count variable
tweet_count = 0

# Search for tweets
tweets = tweepy.Cursor(api.search_tweets, q=keyword, since=start_date, until=end_date, tweet_mode='extended').items()

# Iterate over tweets
for tweet in tweets:
    tweet_count += 1

# Print the count
print(f"Number of tweets related to '{keyword}' between {start_date} and {end_date}: {tweet_count}")