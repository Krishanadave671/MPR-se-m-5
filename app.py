import locationtagger
import nltk
import spacy
nltk.downloader.download('maxent_ne_chunker')
nltk.downloader.download('words')
nltk.downloader.download('treebank')
nltk.downloader.download('maxent_treebank_pos_tagger')
nltk.downloader.download('punkt')
nltk.download('averaged_perceptron_tagger')
text  = "@KawaTweets We have escalated your request with Dahisar Traffic Division for necessary action."
place_entities = locationtagger.find_locations(text = text)
print(place_entities.other_countries)