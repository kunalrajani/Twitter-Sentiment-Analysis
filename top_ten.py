import sys
import json
import re
from collections import Counter 
tagCounts = Counter()

tweet_file = open(sys.argv[1])
line = tweet_file.readlines()
hashtags = []

for i in range(len(line)):
	tweet = json.loads(line[i])
	if tweet.has_key("entities"):
		if len(tweet["entities"]["hashtags"]) !=0 :
			tag = tweet["entities"]["hashtags"][0]["text"].encode('utf-8')
			tagCounts[tag] += 1

topten = tagCounts.most_common(10)

for i in range(len(topten)):
	print topten[i][0], topten[i][1]

