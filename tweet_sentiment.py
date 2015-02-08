import sys
import json
import re

def hw(sent_file):
	afinnfile = sent_file
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	#print scores.items() # Print every (term, score) pair in the dictionary
	return scores

def lines(fp):
    print str(len(fp.readlines()))


def score(str, scores):
	nonalpha = re.compile(r'[^a-z]+')
	words = nonalpha.split(str.lower())	
	senti_scores = 0
	for i in range(len(words)):
		word = words[i]
		if ( (re.match('[a-z]+',word) is not None) & scores.has_key(word)):
			senti_scores = senti_scores + scores[word]
	return float(senti_scores)
	
	
def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	score_map = hw(sent_file)
	line = tweet_file.readlines()
	senti_score = []
	for i in range(len(line)):
	  tweet = json.loads(line[i])
	  if tweet.has_key("text"):
		string = tweet["text"].encode('utf-8')
		print score(string, score_map)
	  else:
	    print 0.0
	#print senti_score
	#type(json.load(line))

if __name__ == '__main__':
    main()
