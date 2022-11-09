
import spacy
from spacy import displacy 
nlp = spacy.load('en_core_web_sm')#
nlp_wk = spacy.load('xx_ent_wiki_sm')
doc = nlp_wk(" We have escalated your request with Dahisar Traffic Division for necessary action.")#
print(doc)