from train import dataset
from keywords import filtered_keywords
from evaluate import evaluate
from utils import draw_table
import os

topic   = 'Illusion'
f       = open('sample_input.txt', 'r')
article = f.read()

corpus, dataset_keywords = dataset(topic)
article_keywords         = filtered_keywords(article)
keywords_set             = dataset_keywords.append(article_keywords)

avg_tf_idf_set, article_tf_idf_set = evaluate(dataset_keywords)

print("=====avg_tf_idf_set=====")
print(avg_tf_idf_set)
print("=====article_tf_idf_set=====")
print(article_tf_idf_set)
draw_table(avg_tf_idf_set, article_tf_idf_set)
