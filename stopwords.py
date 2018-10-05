from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from config import print_list
  
example_sent = "This is a sample sentence, showing off the stop words filtration."
  
stop_words = set(stopwords.words('english')) 
  
word_tokens = word_tokenize(example_sent) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 

print_list(filtered_sentence)