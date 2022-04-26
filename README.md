# Tweet Collector
Utilize `tweetpy` to collect tweets using tweet IDs via API.

## Usage
```python
tweet_id = "937349434668498944"
api_key_filepath = "tweet_api_key.json"
collector = TweetCollector(api_key_filepath)
tweet = collector.collect_tweets_by_id(tweet_id)
with open("test_collected_tweet.json", "w") as f:
    json.dump(tweet, f, indent=4)
```
