from train import data_set
from keywords import filtered_keywords
from evaluate import evaluate
from utils import draw_hash
import os

topic   = 'Illusion'
f       = open('sample_input.txt', 'r')
article = f.read()

corpus, data_set_keywords = data_set(topic)
article_keywords          = filtered_keywords(article)
tf_idf, avg_tf_idf        = evaluate(article_keywords, data_set_keywords)
title                     = f'Avg tf-idf is {avg_tf_idf}'

print(tf_idf)
draw_hash(tf_idf, title)