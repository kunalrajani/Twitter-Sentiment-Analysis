import sys
import json
import re
from collections import Counter 
positive_cnt = Counter()
negative_cnt = Counter()

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
		if tweet.has_key("text"):
			string = tweet["text"].encode('utf-8')
			output = (score(string, score_map))
			senti_score = output[0]
			no_scores = output[1]
			for j in range(len(no_scores)):
				if (senti_score>0):
					positive_cnt[no_scores[j]] += senti_score
				if (senti_score<0):
					negative_cnt[no_scores[j]] += -senti_score
				no_score_terms.append(no_scores[j])
	
	
	neg_dict = dict(negative_cnt)
	pos_dict = dict(positive_cnt)
	#print neg_dict,"\n\n",pos_dict, "\n\n"#[no_score_terms[1]]
	no_score_terms = list(set(no_score_terms))
	
	for i in range(len(no_score_terms)):
		if(neg_dict.has_key(no_score_terms[i]) & pos_dict.has_key(no_score_terms[i])):
			senti_score = float(pos_dict[no_score_terms[i]]/neg_dict[no_score_terms[i]])
			print no_score_terms[i],senti_score
		elif(pos_dict.has_key(no_score_terms[i])):
			print no_score_terms[i],float(pos_dict[no_score_terms[i]])
		else:
			print no_score_terms[i],0.00
	
	#for i in range
	#print senti_score
	#type(json.load(line))

if __name__ == '__main__':
    main()
