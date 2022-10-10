from fileinput import filename
import shutil
from unittest import result
from werkzeug.utils import secure_filename
from nltk.tokenize import word_tokenize
import nltk
import itertools
from gensim.corpora import Dictionary
from collections import defaultdict
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
from flaskext.markdown import Markdown
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.models.tfidfmodel import TfidfModel
from flask import Flask,render_template,request
import Spacy 
import fakenews as fake
import sentiment as stm

app = Flask(__name__, template_folder='template')
Markdown(app)
import os
app.config["UPLOAD_FOLDER"] = "files"
parth = os.getcwd() + "/files"

@app.route('/')
def first_page():
    return render_template('web.html')

@app.route('/upload', methods = ['POST'])   
def upload():
    # if (os.listdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), "files"))) != [] :
    #     shutil.rmtree(".\\files\\")
    f = request.files.getlist('upload[]')
    for a in f :
        dir = os.path.join(parth,a.filename)
        a.save(dir)
    return render_template("web.html")


@app.route('/search', methods = ['POST'])   
def search():
    
    if request.method == 'POST':
        search_words = request.form['search']
        dir_path = r'./files/'
        count = 0
        
        for path in os.listdir(dir_path):
        
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1

    articles = []
    for i in (os.listdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), "files"))) :
        f = open(".\\files\\"+ i, "r")
        article = f.read()
        tokens = word_tokenize(article)
        lower_tokens = [t.lower() for t in tokens]
        alpha_only = [t for t in lower_tokens if t.isalpha()]
        no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
        wordnet_lemmatizer = WordNetLemmatizer()
        lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
        articles.append(lemmatized)
    
    dictionary = Dictionary(articles)
    word_id = dictionary.token2id.get(search_words)
    found = ("Found : "+ search_words +' word id = '+ str(word_id))
    return render_template("web.html",found = found )

@app.route('/compare', methods = ['POST'])   
def compare():
    if request.method == 'POST':
        
        articles = []
        for i in (os.listdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), "files"))) :
            f = open(".\\files\\"+ i, "r")
            article = f.read()
            tokens = word_tokenize(article)
            lower_tokens = [t.lower() for t in tokens]
            alpha_only = [t for t in lower_tokens if t.isalpha()]
            no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
            wordnet_lemmatizer = WordNetLemmatizer()
            lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
            articles.append(lemmatized)
    
        #BOW
        bow = []
        total_word_count = defaultdict(int)
        dictionary = Dictionary(articles)
        corpus = [dictionary.doc2bow(a) for a in articles]
        for word_id, word_count in itertools.chain.from_iterable(corpus):
            total_word_count[word_id] += word_count
        # print(total_word_count)  
        sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1], reverse=True)
        for word_id, word_count in sorted_word_count[:5]:
            bow.append(dictionary.get(word_id) + " = " + str(word_count))
    
    
        #TF_IDF
        idf = []
        dictionary = Dictionary(articles)
        corpus = [dictionary.doc2bow(a) for a in articles]
        doc = corpus[0]
        tfidf = TfidfModel(corpus)
        tfidf_weigth = tfidf[doc]
        # print(tfidf_weigth[:5])
        sorted_tfidf_weights = sorted(tfidf_weigth, key=lambda w: w[1], reverse=True)
        for term_id, weight in sorted_tfidf_weights[:5]:
            idf.append(dictionary.get(term_id)+ " = " + str(weight))
    
    
    return render_template("web.html",bow = bow , idf = idf )

@app.route('/spa_sub', methods = ['POST'])
def spa_sub():
    if request.method == 'POST':
        spac = request.form.get('spa_sub')
        display = Spacy.spa(spac)
    return render_template('spa.html', display=display)

@app.route('/spac')
def spac():
    return render_template('spa.html')

@app.route('/fakenews', methods = ['POST'])
def get_prediction():
    if request.method == 'POST':
        fakenews = request.form.get('fake-news')
        display = fake.get_prediction(fakenews, convert_to_label=True)
    return render_template('fakenews.html', display=display)

@app.route('/fakenews')
def fakenews():
    return render_template('fakenews.html')

@app.route('/sentiment', methods = ['POST'])
def sentiment_check():
    if request.method == 'POST':
        sentiment = request.form.get('sentiment')
        display = stm.sentiment_check(sentiment)
    return render_template('sentiment.html', display=display)

@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')

if __name__ == '__main__':
    app.run(debug=True)