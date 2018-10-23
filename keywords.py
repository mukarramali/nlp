from rake_nltk import Rake
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from config import to_s, sample_text, breakpoint

def remove_stopwords(text):
	print("=======Removing stopwords from new article========")
	stop_words = set(stopwords.words('english')) 
	word_tokens = word_tokenize(text) 	  
	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	return filtered_sentence

def ranked_keyword(text):
	r = Rake()
	r.extract_keywords_from_text(text.decode("utf-8"))
	ranked_keyword = r.get_ranked_phrases_with_scores()
	return len(ranked_keyword) < 50 and ranked_keyword or ranked_keyword[0:50]

# keywords = ranked_keyword(sample_text())
# print(to_s(keywords))
