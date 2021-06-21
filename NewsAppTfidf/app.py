# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 19:01:53 2021

@author: Shubham
"""

# coding=utf-8

import os
import threading
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
import re


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from nltk.corpus import stopwords 
import re
import contractions
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from gensim.models import Doc2Vec
lemmatizer = WordNetLemmatizer()

# Flask utils
from flask import Flask, request, render_template, jsonify

import time

import pickle
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


app = Flask(__name__)

PATH = "C:\Program Files (x86)\chromedriver.exe"


chrome_options = Options()

chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")



#LOAD MODEL
loaded_vec = CountVectorizer(vocabulary=pickle.load(open("count_vector.pkl", "rb")))
loaded_tfidf = pickle.load(open("tfidf.pkl","rb"))
loaded_model = pickle.load(open("tfidf_clf_model.pkl","rb"))


class_list = ['Books', 'Business', 'Cricket', 'Education', 'Elections', 'Entertainment', 'Environment', 'Football', 'Health', 'International', 'Life & Style', 'National', 'Other Sports', 'Sci-Tech', 'Society', 'Tennis']

app = Flask(__name__)
basepath = os.path.dirname(__file__)

def get_article_text(link):
    ###########
    driver = webdriver.Chrome(options=chrome_options, executable_path= PATH)
    driver.get(link)
    time.sleep(3)
    txt = ""
    try:
        content = driver.find_element_by_css_selector('[id^=content-body]')
        para = content.find_elements_by_tag_name('p')
    except :
        return txt
    else:
        for i in range(len(para)):
            txt = txt + " " + para[i].text
        return txt


def process_text(text):
    
    expanded_words = []    
    for word in text.split():
      # using contractions.fix to expand the shotened words
      expanded_words.append(contractions.fix(word))   

    text = ' '.join(expanded_words)
    
    text = text.lower().replace('\n',' ').replace('\r','').replace('-', ' ').strip()
    text = re.sub(' +', ' ', text)
    text = re.sub(r'[^\w\s]','',text)
    text = re.sub(r'\d+', '', text)   # remove numbers
    
    
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(text) 
    filtered_sentence = [] 
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
    
    lemmas = []
    for word in filtered_sentence:
        lemmas.append(lemmatizer.lemmatize(word, pos ='v'))
    
    text = " ".join(lemmas)
    
    txt = []
    word_tokens = word_tokenize(text) 
    for w in word_tokens:
        txt.append(lemmatizer.lemmatize(w, pos ='n'))
    text = " ".join(txt)
    
    return text


@app.route('/', methods=['GET'])
def index():
    ##basepath = os.path.dirname(__file__)
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        link = request.form['articleUrl']
        print(link)
        text = get_article_text(link)
        preprocessed = process_text(text)
        print(preprocessed)
        
        docs_new = [preprocessed]

        X_new_counts = loaded_vec.transform(docs_new)
        X_new_tfidf = loaded_tfidf.transform(X_new_counts)
        predicted = loaded_model.predict(X_new_tfidf)
               
        result = class_list[predicted[0]]
    
        print(result) 
        return result
    return None
        
        
        
if __name__=="__main__":
    app.run(debug=True)
        
    
