from nltk.stem import PorterStemmer, WordNetLemmatizer
 
stemmer = PorterStemmer()
lemmatiser = WordNetLemmatizer()

word = "coding"
 
print("Stem %s: %s" % (word, stemmer.stem(word)))
print("Lemmatise %s: %s" % (word, lemmatiser.lemmatize(word)))
print("Lemmatise %s: %s" % (word, lemmatiser.lemmatize(word, pos="v")))