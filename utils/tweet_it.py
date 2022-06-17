"""imports"""
from datetime import datetime
import json
from random import randint
import time
import calendar
import tweepy
import os
"""Main Class for perfoming different Task"""

class tweet_it():
    def __init__(self) -> None:
        """__init__ function: This function Connects to Twitter Account and create api object for it."""
        try:
            CONSUMER_KEY = os.getenv('CONSUMER_KEY')
            CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
            ACCESS_KEY = os.getenv('ACCESS_KEY')
            ACCESS_SECRET = os.getenv('ACCESS_SECRET')
            auth = tweepy.OAuth1UserHandler(CONSUMER_KEY,CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
            api = tweepy.API(auth=auth)
            self.api = api
            self.hashtable = {"programming_quotes":[],"motivational_quotes":[]}
        except ConnectionError as e:
            print(e)
    def authenticate(self):
        """Authentication Function for tweet_it class"""
        try:
            self.api.verify_credentials()
            return True
        except ConnectionRefusedError as e:
            return False
    def get_day(self):
        day = datetime.today()
        date = '2021-05-21'
        all = datetime.strptime(date,'%Y-%m-%d')
        day_name = calendar.day_name[day.weekday()]
        month_name = calendar.month_name[all.month]
        year = all.year
        return [day.day,month_name,year,day_name]

    def good_morning_tweet(self):
        """Good Morning Tweet Function"""
        day,month_name,year,day_name = self.get_day()
        status = f"{day} {month_name} {year}\nGood Morning Everyone\nHappy {day_name}\nKeep Smiling and Keep Grinding"
        self.api.update_status(status=status)

    def good_afternoon_tweet(self):
        """Good AfterNoon Tweet Function"""
        day,month_name,year,day_name = self.get_day()
        status = f"{day} {month_name} {year}\nGood afternoon Everyone\nHow is Your {day_name} going?"
        self.api.update_status(status=status)

    def good_evening_tweet(self):
        """Good Evening Tweet Function"""
        day,month_name,year,day_name = self.get_day()
        status = f"{day} {month_name} {year}\nGood Evening Everyone\nWhat's your plan for {day_name} Evening?"
        self.api.update_status(status=status)

    def good_night_tweet(self):
        """Good Night Tweet Function"""
        day,month_name,year,day_name = self.get_day()
        status = f"{day} {month_name} {year}\nGood Night Everyone\nI'm going to Sleep Now zZz \nHow was your {day_name}?"
        self.api.update_status(status=status)
    
    def test(self):
        day,month_name,year,day_name = self.get_day()
        self.api.update_status(f"{day} {month_name} {year}\nTesting Twitter Bot on {day_name}")

    def fetch_quotes(self,filename):
        """It fetch all quotes from json file"""
        file = os.path.join(filename)
        # print(file)
        with open(f"./utils/{file}","r") as f:
            data = f.read()
        quotes = json.loads(data)
        return quotes
    
    def tweet(self,filename,hashtag):
        """Tweet using Fetched Quotes"""
        quotes = self.fetch_quotes(f"{filename}.json")
        i = randint(1,len(quotes))
        for quote in quotes:
            if len(quote['text'])>250:
                continue
            if  quote['id'] == i and quote['id'] not in self.hashtable[f"{filename}"]:
                self.api.update_status(f"{hashtag}\n{quote['text']}")
                self.hashtable[f"{filename}"].append(quote['id'])
    def programming_quotes(self):
        """For tweeting Programming Quotes"""
        self.tweet("programming_quotes","#programming,#programming-quotes")
        
    def motivational_quotes(self):
        """For tweeting Motivational Quotes"""
        self.tweet("motivational_quotes","#motivation,#motivation-quotes")

    def anime_quotes(self):
        pass

    def run(self):
        """Main function: use run function for starting Bot"""
        if(self.authenticate()):
            while True:
            		# it can be change according to your preference
                self.good_evening_tweet()
                time.sleep(60*30)
                self.programming_quotes()
                time.sleep(60*30)
                self.motivational_quotes()
                time.sleep(60*60*4)
                self.good_night_tweet()
                time.sleep(60*60*8)
                self.good_morning_tweet()
                time.sleep(60*30)
                self.motivational_quotes()
                time.sleep(60*30)
                self.motivational_quotes()
                time.sleep(60*60*7)
                self.good_afternoon_tweet()
                time.sleep(60*60*5)


