from functools import total_ordering
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
computer_id = dictionary.token2id.get("computer")
corpus = [dictionary.doc2bow(a) for a in articles]
doc = corpus[0]
bow_doc = sorted(doc,key=lambda w: w[1], reverse=True)

# for word_id, word_count in bow_doc[:10]:
#     print(dictionary.get(word_id),word_count)

total_word_count = defaultdict(int)
for word_id, word_count in itertools.chain.from_iterable(corpus):
    total_word_count[word_id] += word_count
# print(total_word_count)  
sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1], reverse=True)
for word_id, word_count in sorted_word_count[:5]:
    print(dictionary.get(word_id), word_count)

# for n in range(10) :
#     print(articles[n])
#     print('\n')



