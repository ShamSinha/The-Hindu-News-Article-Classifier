# The-Hindu-News-Article-Classifier

## Installations 

1. [Install Anaconda](https://docs.anaconda.com/anaconda/install/)
2. There are certain dependencies should be installed in your conda environment to work this web app in your local machine.
     - nltk
     - gensim=4.0.1
     - joblib
     - contractions
     - re
     - scikit-learn=0.24.1
3. Need Selenium Chrome WebDriver for scraping the text of the article given its url in web app.
      
## To run web app 
 1. Clone this repo.
 2. Download this [folder](https://drive.google.com/drive/folders/1WPUT9Fk_I7akEMG0pY-F1GpBj62ZETyz?usp=sharing) from Google Drive to get our trained Doc2Vec model for our training dataset. Include all its files in NewsApp directory.
 3. Update the PATH variable present in app.py to installation path location of chromedriver.exe
 4. Run *app.py* in Spyder.
 5. Open [local address](http://127.0.0.1:5000/) in a browser.

## Web App

![](https://github.com/ShamSinha/The-Hindu-News-Article-Classifier/blob/main/Screenshot%20(543).png)
![](https://github.com/ShamSinha/The-Hindu-News-Article-Classifier/blob/main/Screenshot%20(545).png)
![](https://github.com/ShamSinha/The-Hindu-News-Article-Classifier/blob/main/Screenshot%20(546).png)



### Dataset 

Web Scraping is used on [The Hindu website](https://www.thehindu.com/archive/web/) to extract text data for different news topics.

Data Scraped is stored in [ArticlesDatabaseM](https://drive.google.com/file/d/1mw3FCoCc2QcCBecX8R-RzpAFks2btXc_/view?usp=sharing) file.
In this database articles text are stored in **articles_link_tb** sqlite table after preprocessing of text. 

For Implementation See [ScrapeLinks](/ScrapeLinks.ipynb) and [ArticleExt&Prep](/ArticleExt&Prep.ipynb) jupyter notebook files.



| News_Topic    | Num_Articles  |
| :-------------: | :-------------: |
|Life & Style   |  4641 |
|Business       |  4434 |
|Sci-Tech       |  3772 |
|Entertainment  |  3723 |
|Other Sports   |  3664 |
|Elections      |  3593 |
|Society        |  3591 |
|Tennis         |  2915 |
|Education      |  2743 |
|International  |  2726 |
|National       |  2520 |
|Football       |  2491 |
|Cricket        |  2437 |
|Books          |  1944 |
|Health         |  1905 |
|Environment    |  1864 |

Data is split into 75% train set and 25% test set.

## Two different model is used to Learn Document Embeddings

### 1. Doc2Vec             

Learn paragraph and document embeddings via the distributed bag of words models shown in this [paper](https://arxiv.org/pdf/1405.4053v2.pdf).

**[See Reference](https://radimrehurek.com/gensim/models/doc2vec.html)**

For Implementation See [TrainClassifier](/TrainClassifier.ipynb) for given Dataset.

#### Classification Report

|News_Topic|precision|recall|f1-score|support|
| :-----:  | :----: | :------: | :-----: | :----: |
|Books|0.76|0.79|0.77|490|
|Business|0.87|0.88|0.88|1109|
|Cricket|0.95|0.96|0.95|610|
|Education|0.79|0.79|0.79|671|
|Elections|0.90|0.94|0.92|919|
|Entertainment|0.79|0.78|0.78|919|
|Environment|0.71|0.72|0.71|492|
|Football|0.96|0.96|0.96|614|
|Health|0.67|0.70|0.69|460|
|International|0.82|0.80|0.81|711|
|Life & Style|0.70|0.73|0.71|1129|
|National|0.69|0.65|0.67|624|
|Other Sports|0.94|0.95|0.94|912|
|Sci-Tech|0.77|0.76|0.76|992|
|Society|0.67|0.61|0.64|905|
|Tennis|0.97|0.98|0.98|684|
|accuracy|||0.81|12241|

### 2. TF-IDF 
Tf means term-frequency while tf-idf means term-frequency times inverse document-frequency. This is a common term weighting scheme in information retrieval, that has also found good use in document classification.

**[See Reference](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html)**

For Implementation See [TrainClassifier2](/TrainClassifier2.ipynb) for given Dataset.

#### Classification Report

|News_Topic|precision|recall|f1-score|support|
| :-----:  | :----: | :------: | :-----: | :----: |
|Books|0.87|0.71|0.78|544|
|Business|0.90|0.91|0.90|1078|
|Cricket|0.98|0.98|0.98|633|
|Education|0.81|0.90|0.85|686|
|Elections|0.91|0.94|0.93|920|
|Entertainment|0.81|0.86|0.83|977|
|Environment|0.71|0.77|0.74|473|
|Football|0.99|0.99|0.99|636|
|Health|0.73|0.66|0.69|475|
|International|0.81|0.85|0.83|642|
|Life & Style|0.78|0.67|0.72|1164|
|National|0.73|0.67|0.70|618|
|Other Sports|0.97|0.97|0.97|911|
|Sci-Tech|0.84|0.75|0.79|938|
|Society|0.60|0.73|0.66|857|
|Tennis|0.99|0.98|0.98|689|
|accuracy|||0.84| 12241|


 
 
 
 
