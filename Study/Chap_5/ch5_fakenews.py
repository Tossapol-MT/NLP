from turtle import title
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
import re
from nltk.stem.porter import PorterStemmer
from collections import Counter

# load the dataset
news_d = pd.read_csv('.\\fake-news\\train.csv')

# print("Shape of News data:", news_d.shape)
# print("News data columns", news_d.columns)
# print(news_d.head())

txt_length = news_d.text.str.split().str.len()
# print(txt_length.describe())
title_lenght = news_d.title.str.split().str.len()
# print(title_lenght.describe()).

sns.countplot(x="label", data=news_d);
# print("1: Unreliable")
# print("0: Reliable")
# print("Distribution of labels:")
# print(news_d.label.value_counts());

# Constants that are used to clean the datasets
column_n = ['id', 'title', 'author', 'text', 'label']
remove_c = ['id','author']
categorical_features = []
target_col = ['label']
text_f = ['title', 'text']

ps = PorterStemmer()
wnl = nltk.stem.WordNetLemmatizer()

stop_words = stopwords.words('english')
stopwords_dict = Counter(stop_words)

# Removed unused clumns
def remove_unused_c(df,column_n=remove_c):
    df = df.drop(column_n,axis=1)
    return df

# Impute null values with None
def null_process(feature_df):

    for col in text_f:
        feature_df.loc[feature_df[col].isnull(), col] = "None"
    return feature_df

def clean_dataset(df):
    # remove unused column
    df = remove_unused_c(df)
    #impute null values
    df = null_process(df)
    return df
# Cleaning text from unused characters
def clean_text(text):
    # removing urls
    text = str(text).replace(r'http[\w:/\.]+', ' ')

    # remove everything except characters and punctuation
    text = str(text).replace(r'[^\.\w\s]', ' ')
    text = str(text).replace('[^a-zA-Z]', ' ')
    text = str(text).replace(r'\s\s+', ' ')
    text = text.lower().strip()
    return text

## Nltk Preprocessing include:
# Stop words, Stemming and Lemmatization
# For our project we use only Stop word removal
def nltk_preprocess(text):
    text = clean_text(text)
    wordlist = re.sub(r'[^\w\s]','', text).split()
    text = ' '.join([wnl.lemmatize(word) for word in
wordlist if word not in stopwords_dict])
    return text

# Perform data cleaning on train and test dataset by callingclean_dataset function
df = clean_dataset(news_d)
# apply preprocessing on text through apply method by callingthe function nltk_preprocess
df["text"] = df.text.apply(nltk_preprocess)
# apply preprocessing on title through apply method by callingthe function nltk_preprocess
df["title"] = df.title.apply(nltk_preprocess)
# Dataset after cleaning and preprocessing step
# print(df.head())


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
# initialize the word cloud
wordcloud = WordCloud( background_color='black', width=800, height=600)
# generate the word cloud by passing the corpus
text_cloud = wordcloud.generate(' '.join(df['text']))
# plotting the word cloud
plt.figure(figsize=(20,30))
plt.imshow(text_cloud)
plt.axis('off')
plt.show()

# Word cloud for reliable news only:
true_n = ' '.join(df[df['label']==0]['text'])
wc = wordcloud.generate(true_n)
plt.figure(figsize=(20,30))
plt.imshow(wc)
plt.axis('off')
plt.show()

# Word cloud for fake news only:

fake_n = ' '.join(df[df['label']==1]['text'])
wc= wordcloud.generate(fake_n)
plt.figure(figsize=(20,30))
plt.imshow(wc)
plt.axis('off')
plt.show()

def plot_top_ngrams(corpus, title, ylabel, xlabel="Number of Occurences", n=2):
    """Utility function to plot top n-grams"""
    true_b = (pd.Series(nltk.ngrams(corpus.split(), n)).value_counts())[:20]
    true_b.sort_values().plot.barh(color='blue', width=.9, figsize=(12, 8))
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()

plot_top_ngrams(true_n, 'Top 20 Frequently Occuring True news Bigrams', "Bigram", n=2)

# The most common bigram on the fake news:
plot_top_ngrams(fake_n, 'Top 20 Frequently Occuring Fake news Bigrams', "Bigram", n=2)
    
# The most common trigram on reliable news:
plot_top_ngrams(true_n, 'Top 20 Frequently Occuring True news Trigrams', "Trigrams", n=3)

# For fake news now:
plot_top_ngrams(fake_n, 'Top 20 Frequently Occuring Fake news Trigrams', "Trigrams", n=3)