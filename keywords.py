from rake_nltk import Rake
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

from config import print_list, sample_text

def remove_stopwords(text):
	stop_words = set(stopwords.words('english')) 
	word_tokens = word_tokenize(text) 	  
	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	return filtered_sentence

def ranked_keyword(text):
	r = Rake()
	r.extract_keywords_from_text(text)
	return r.get_ranked_phrases_with_scores()[0:10]

keywords = ranked_keyword(sample_text())

print_list(keywords)