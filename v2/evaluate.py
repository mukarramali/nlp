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

def normalize_avg_tf_idf(avg_tfidf_set, data_set_keywords):
	for key in set(avg_tfidf_set):
		avg_tfidf_set[key] = avg_tfidf_set[key]/search_in_docs(key, data_set_keywords)
	return avg_tfidf_set

def evaluate(data_set_keywords):
	list_tf_idf_set = []
	avg_tfidf_set   = {}
	for article_keywords in data_set_keywords:
		tf_idf_set = {}
		for key in set(article_keywords):
			tf_idf_set[key]     = tf_idf(key, article_keywords, data_set_keywords)
			if avg_tfidf_set.get(key) == None: avg_tfidf_set[key] = 0
			avg_tfidf_set[key] += tf_idf_set[key]
		list_tf_idf_set.append(tf_idf_set)
	return normalize_avg_tf_idf(avg_tfidf_set, data_set_keywords), list_tf_idf_set[-1]
