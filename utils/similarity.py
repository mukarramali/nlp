import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en_core_web_lg')

# Determine semantic similarities
doc1 = nlp(u"my fries were super gross")
doc2 = nlp(u"such super bad tomato")
similarity = doc1.similarity(doc2)
print("similarity is:", similarity)



# # Process whole documents
# text = (u"When Sebastian Thrun started working on self-driving cars at "
#         u"Google in 2007, few people outside of the company took him "
#         u"seriously. “I can tell you very senior CEOs of major American "
#         u"car companies would shake my hand and turn away because I wasn’t "
#         u"worth talking to,” said Thrun, now the co-founder and CEO of "
#         u"online higher education startup Udacity, in an interview with "
#         u"Recode earlier this week.")
# doc = nlp(text)

# # Find named entities, phrases and concepts
# for entity in doc.ents:
#     print(entity.text, entity.label_)