from wiki import wikies
from keywords import ranked_keyword
from config import to_s

def data_set(topic):
	topics, articles = wikies(topic)
	corpus 			 = []
	keywords         = []
	print("=======Getting data set for {0}========".format(topic))
	for index in range(len(topics)):
		keys = ranked_keyword(articles[index])
		corpus.append({'topic': topics[index], 'keywords': keys})
		keywords.append(keys)

	return corpus, keywords
