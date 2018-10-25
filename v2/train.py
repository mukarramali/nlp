from wiki import wikies
from keywords import ranked_keyword, filtered_keywords

def dataset(topic):
	topics, articles = wikies(topic)
	corpus 			 = []
	keywords         = []
	print("=======Getting data set for {0}========".format(topic))
	for index in range(len(topics)):
		keys = filtered_keywords(articles[index])
		corpus.append({'topic': topics[index], 'keywords': keys})
		keywords.append(keys)

	return corpus, keywords
