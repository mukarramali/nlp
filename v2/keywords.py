from rake_nltk import Rake
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
stemmer = PorterStemmer()

def remove_stopwords(text):
	stop_words  = set(stopwords.words('english'))
	word_tokens = word_tokenize(str(text))
	return [w for w in word_tokens if not w in stop_words and w.isalpha()]

def stem(words):
	if type(words) != list: words = [words]
	return [stemmer.stem(w) for w in words]

def filtered_keywords(text):
	without_stopwords = remove_stopwords(text)
	keywords          = stem(without_stopwords)
	return list(set(keywords))

def ranked_keyword(text):
	r = Rake()
	r.extract_keywords_from_text(text.decode("utf-8"))
	ranked_keyword = r.get_ranked_phrases_with_scores()
	return len(ranked_keyword) < 50 and ranked_keyword or ranked_keyword[0:50]
