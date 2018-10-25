from newspaper3k import Article

def article_keywords(link):
	article_name = Article(url, language="en")
	article_name.download()
	article_name.parse()
	article_name.nlp()
	return article_name.keywords

# link = "https://www.indiewire.com/2018/10/venom-post-credits-scenes-explained-spider-verse-1202009299/"
# print(article_keywords(link))