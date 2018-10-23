from train import data_set
from keywords import remove_stopwords
from config import to_s

topic   = 'Illusion'
f       = open("sample_input.txt", "r")
article = f.read()

corpus, keywords = data_set(topic)

article_keywords = list(set(remove_stopwords(article)))

def search(keywords, training_data):
	print("=======Searching data set occurance in given article========")
	occurance = 0
	count = 0
	for key in keywords:
		freq = training_data.count(key)
		occurance += freq
		count += 1 if freq > 0 else 0
	return count, occurance

matched, ranking = search(article_keywords, to_s(keywords, " "))

print("{0}({1}) out of {2} matches".format(matched, ranking, len(article_keywords)))
