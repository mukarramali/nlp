import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

s = "This is a simple sentence Generate list of tokens"
tokens = word_tokenize(s) # Generate list of tokens
tokens_pos = pos_tag(tokens)

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(tokens_pos)

print(result)

result.draw()
