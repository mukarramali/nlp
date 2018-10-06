from scrap import wikies
from keywords import ranked_keyword
from config import to_s

topic = "Illusion"

topics, articles = wikies(topic)

clustors = []

for index in range(len(topics)):
	keywords = ranked_keyword(articles[index])
	clustors.append({'topic': topics[index], 'article': articles[index], 'keywords': keywords})

print(to_s(clustors))