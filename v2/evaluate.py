from math import log
from utils import max_freq
from IPython import embed

def search_in_docs(key, data_set_keywords):
	count = 0
	for keywords_list in data_set_keywords:
		if keywords_list.count(key) > 0: count += 1
	if count == 0: count +=1
	return count+1

def tf_idf(key, keywords, data_set_keywords):
	count = keywords.count(key)
	tf    = 0.5 + 0.5 * keywords.count(key)/max_freq(keywords)
	idf   = log(len(data_set_keywords)/search_in_docs(key, data_set_keywords))
	return tf * idf

def evaluate(keywords, data_set_keywords):
	tf_idf_set = {}
	avg_tfidf  = 0
	for key in keywords:
		if tf_idf_set.get(key) != None: continue
		tf_idf_set[key]         = tf_idf(key, keywords, data_set_keywords)
		avg_tfidf              += tf_idf_set[key]
	return tf_idf_set, avg_tfidf/len(set(keywords))
