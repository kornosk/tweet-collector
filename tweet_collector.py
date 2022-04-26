#!/usr/bin/env python
# coding: utf-8

'''
@title: Utilities for working on Twitter data
@authors: Kornraphop Kawintiranon (Ken)
@institution: Georgetown University
@project: Tweet Collector
@date: April 2022
@updated: April 2022
@description: Utilities for working on Twitter data
'''


import json
import tweepy


class TweetCollector():
    """ A class to collect tweets. """

    def __init__(self, api_key_filepath):
        # Read credential file
        with open(api_key_filepath, "r") as f:
            data = json.load(f)
        consumer_key = data["app_key"]
        consumer_secret = data["app_secret"]
        access_token = data["oauth_token"]
        access_token_secret = data["oauth_token_secret"]

        # Init API client
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    def collect_tweets_by_id(self, tweet_id):
        try:
            status = self.api.get_status(tweet_id, tweet_mode="extended")
        except Exception as e:
            status = {
                "id_str": str(tweet_id),
                "error": str(e)
            }
        return status if isinstance(status, dict) else status._json


def main():
    tweet_id = "937349434668498944"
    api_key_filepath = "tweet_api_key.json"
    collector = TweetCollector(api_key_filepath)
    tweet = collector.collect_tweets_by_id(tweet_id)
    with open("test_collected_tweet.json", "w") as f:
        json.dump(tweet, f, indent=4)


if __name__ == "__main__":
    main()