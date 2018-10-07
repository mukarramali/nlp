from train import data_set
from keywords import remove_stopwords
from to_s import config

topic   = 'Illusion'
f       = open("sample.txt", "r")
article = f.read()

corpus, keywords = data_set(topic)

article_keywords = list(set(remove_stopwords(article)))

def search(keywords, training_data):
	count = 0
	for key in keywords:
		count += training_data.count(key)
	return count

ranking = search(article_keywords, to_s(keywords, " "))