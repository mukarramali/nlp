import wikipedia

def wikies(thing):
	suggested_topics = wikipedia.search(thing)
	articles 		 = []
	topics   		 = []
	for topics in suggested_topics:
		wiki = wikipedia.page(topics)
		articles.append(str(wiki.content))
		topics.append(str(wiki.title))
	return articles