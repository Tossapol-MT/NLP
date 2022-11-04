from cgi import print_environ
from functools import total_ordering
from logging.config import dictConfig
from re import T
import nltk
import itertools

from gensim.corpora import Dictionary
from collections import defaultdict
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.models.tfidfmodel import TfidfModel

articles = []
for i in range(10) :
    f = open(f"wiki_article_{i}.txt", "r")
    article = f.read()
    tokens = word_tokenize(article)
    lower_tokens = [t.lower() for t in tokens]
    alpha_only = [t for t in lower_tokens if t.isalpha()]
    no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
    articles.append(lemmatized)
    
dictionary = Dictionary(articles)
corpus = [dictionary.doc2bow(a) for a in articles]
doc = corpus[9]
tfidf = TfidfModel(corpus)
tfidf_weigth = tfidf[doc]
# print(tfidf_weigth[:5])
sorted_tfidf_weights = sorted(tfidf_weigth, key=lambda w: w[1], reverse=True)
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary.get(term_id), weight)
