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



### Doc2Vec For Learning Document Embeddings                  **[See Reference](https://radimrehurek.com/gensim/models/doc2vec.html)**

Learn paragraph and document embeddings via the distributed bag of words models shown in this [paper](https://arxiv.org/pdf/1405.4053v2.pdf).



### Classification Report

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

 
 
 
 
