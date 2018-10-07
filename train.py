from wiki import wikies
from keywords import ranked_keyword
from config import to_s

def data_set(topic):
	topics, articles = wikies(topic)
	corpus 			 = []
	keywords         = []
	for index in range(len(topics)):
		keys = ranked_keyword(articles[index])
		corpus.append({'topic': topics[index], 'keywords': keys})
		keywords.append(keys)

	return corpus, list(set(keywords))
