import wikipedia
import unicodedata

def to_str(unicode):
	return unicodedata.normalize('NFKD', unicode).encode('ascii','ignore')

def wikies(thing):
	suggested_topics = wikipedia.search(thing)
	articles 		 = []
	topics   		 = []
	for topic in suggested_topics:
		should_add = input("Is '{0}' related to your context?([y]/n)".format(topic)).lower()
		if should_add != '' and should_add != 'y': continue
		wiki = wikipedia.page(topic)
		articles.append(to_str(wiki.content))
		topics.append(to_str(wiki.title))
	return topics, articles
