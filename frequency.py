import sys
import json
import re

nonalpha = re.compile(r'[^a-z]+')
tweet_file = open(sys.argv[1])
line = tweet_file.readlines()
terms = []
for i in range(len(line)):
	tweet = json.loads(line[i])
	if tweet.has_key("text"):
		string = tweet["text"].encode('utf-8')
		words = nonalpha.split(string.lower())
		for i in range(len(words)):
			terms.append(words[i])
#print terms
for i in range(len(terms)):
	#print terms[i]
	re.sub('^[a-z]$','',terms[i])
terms = filter(None,terms)
#print terms

unique = set(terms)
freq = [terms.count(item)for item in unique]
freq = [float(i) for i in freq]
total_count = sum(freq)
#freq = float(freq/sum(freq)
for i in range(len(freq)):
	freq[i] = freq[i]/total_count
	print unique.pop()," ", freq[i]

