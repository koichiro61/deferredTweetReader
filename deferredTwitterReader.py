# screen name uuuuu の人の tweet を一定間隔更新チェックし、指定時間経過後に表示する
# https://www.pytry3g.com/entry/python-twitter-timeline
# https://docs.tweepy.org/en/v3.5.0/api.html?highlight=user_timeline#API.user_timeline
# "elavated access" is required,
#   which is given to applicants on the developers portal

account = 'screenname'           # screen name
tweets_to_fetch = 10            # max number of tweets to fetch at one time
interval_to_fetch = 15  # in seconds
defer_time = 180        # in seconds200

import tweepy, time
from twitterKeyToken import twitterKeyToken
import datetime
from datetime import timedelta, tzinfo
import sys
import qTweetList
import sched
from sound import *

tz_jst = datetime.timezone(datetime.timedelta(hours=9))

def showTweet(qtw):     # custom printing routine for qTweetlist object
	se = play_effect('arcade:Coin_2')
	qtw.show(tz_jst)
	
	
# ------------------------------ main routine --------------------
# APIの認証
auth = tweepy.OAuthHandler\
        (       twitterKeyToken.API_KEY,
                twitterKeyToken.API_SECRET)
auth.set_access_token\
        (       twitterKeyToken.ACCESS_TOKEN,
                twitterKeyToken.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 最初に過去分 tweet をとってきて qtl に格納
latest_tweet_id = 1
qtl = qTweetList.qTweetList()

# main loop ここから
while(True):
	status_list = api.user_timeline(
	screen_name=account,since_id=latest_tweet_id)
	dt_now = datetime.datetime.now(tz_jst)
	
	if status_list:
		se = play_effect('arcade:Coin_1')
		
		id_list =[]
		for status in status_list: id_list.append(status.id)
		latest_tweet_id = max(id_list)
		
		qtl.statusList = status_list
		qtl.queuedTime = datetime.datetime.now(tz_jst)
		
		# defer_time 経過後に showTweet(qrl)を実行するようスケジュール登録
		s = sched.scheduler()
		s.enter(defer_time, 1, showTweet, argument=(qtl,))
		# scheduler.enter(delay, priority, action, argument=(), kwargs={})
		s.run()
		
	# interval を置いてから main loop の頭に戻る
	time.sleep(interval_to_fetch)
# main loop ここまで

