import sys
import json
import re
from collections import Counter 
state_score = Counter()

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
	no_scores = []
	for i in range(len(words)):
		word = words[i]
		if ( (re.match('[a-z]+',word) is not None) & scores.has_key(word)):
			senti_scores = senti_scores + scores[word]
		if (scores.has_key(word) is False and (re.match('[a-z]{3}',word) is not None)):
			no_scores.append(word)
	return (float(senti_scores),no_scores)
	
	
def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	score_map = hw(sent_file)
	line = tweet_file.readlines()
	senti_score = []
	no_score_terms = []
	for i in range(len(line)):
		tweet = json.loads(line[i])
		if (tweet.has_key("place") & tweet.has_key("text")):
			if(tweet["place"] is not None):
				if(tweet["place"]["country_code"]=="US"):
					state = tweet["place"]["full_name"][-2:]
					string = tweet["text"].encode('utf-8')
					output = (score(string, score_map))
					senti_score = output[0]
					state_score[state] += senti_score
	
	#print neg_dict,"\n\n",pos_dict, "\n\n"#[no_score_terms[1]]
	print state_score.most_common(1)[0][0]
	
	
	
if __name__ == '__main__':
    main()
