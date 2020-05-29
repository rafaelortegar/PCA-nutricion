# Puntos a tratar en la parte de feature engineering:


**NOTA:** De todo copiaré códigos pero hechos en Stata, por si nos ayuda.

1. Primero hay que identificar el tipo de variables, en el cuestionario .docx ya vienen por colores.
        
- Amarillo: Categórica  ordinal.
- Verde: Categórica nominal.
- Azul: Categoría de referencia.
        
2. Hacer el merge de las dos bases por la variable nofolio.

- Tirar las observaciones que no hagan merge pues necesitamos el cuestioarnio de contexto y los puntajes.
        
3. Hay que reemplazar valores faltantes que vienen como ">" por el indicador de faltante en python

        foreach var of varlist p*{
        replace `var' = subinstr(`var',">","",.)
        }

4. Reemplazar los missings de sexo (p1) con la variable de género de la base planea_alumnos_2016.csv.

- OJO: Hay unas que vienen codificadas cono "C" o "D" en vez de "A" para hombre y "B" para mujer. Esas hay que 
    identificarlas y también sustituirlas.  
    
- Hay que codificar A si es hombre y B si es mujer para después poder usar un loop para codificar todo lo demás.

        replace p1=genero if p1==""
        replace p1=genero if p1=="C"
        replace p1=genero if p1=="D"
        replace p1="A" if p1 =="H"
        replace p1="B" if p1 =="M"
        drop sexo

5. Recodificar todas las preguntas de strings a numéricas con un loop. Vienen en orden entonces A=1, B=2 ,...., J=10

        foreach var of varlist p*{
        replace `var' ="1" if `var'=="A"
        replace `var' ="2" if `var'=="B"
        replace `var' ="3" if `var'=="C"
        replace `var' ="4" if `var'=="D"
        replace `var' ="5" if `var'=="E"
        replace `var' ="6" if `var'=="F"
        replace `var' ="7" if `var'=="G"
        replace `var' ="8" if `var'=="H"
        replace `var' ="9" if `var'=="I"
        replace `var' ="10" if `var'=="J"
        }

6. Verificar que no hayan errores de codificación, por ejemplo, la pregunta 69 solo debe tener A=1 y B=2, pero por errores hay respuestas p69=="3" | p69=="4" | p69=="5" | p69=="6" | p69=="7" | p69=="N" | p69=="S". Hay que volver missings esas observaciones

        replace p69 ="" if p69=="3" | p69=="4" | p69=="5" | p69=="6" | p69=="7" | p69=="N" | p69=="S"

- Las que tengo identificadas con errores de codificación son: p6, p69, p72, p73, p75-p77, p79, p81-p84, p87, p88, p109, p118, p130, p131, p132, p134, p137, p140, p145-p150

- Ojo: Pueden haber más, especialmente en la parte de p11-p66 que ya no revisé.

7. Generar dummies para las preguntas que están en verde en el cuestionario. Por ejemplo: p3, p4, p5, p9, etc y renombrarlas como p4_1, p4_2, p4_3, etc.

        tab p3, gen (dummy)
        rename dummy1 p3_1
        rename dummy2 p3_2
        rename dummy3 p3_3

8. Generar dummies para entidad, modalidad, sostenimiento, subsistema (recodificar de la siguiente forma), nvl_esp y nvl_mat.

        replace subsist = "TELEBACH/EMSAD" if subsist =="TELEBACHILLERATOS" | subsist =="TELEBACHILLERATOS COMUNITARIOS" | subsist =="EMSAD"
        replace subsist = "COLBACH/Otros federales" if subsist =="DGETA" | subsist =="DGECYTM" | subsist =="COLBACH"  | subsist =="DGB" | subsist =="CETI" | subsist =="IPN"
        replace subsist = "Particulares/A.C." if subsist =="PARTICULARES" | subsist =="ASOCIACI�N CIVIL"

9. Generar la variable missing que nos diga si hay aunque sea un missing en las preguntas de un alumnos.  

        gen missing =0

        foreach var of varlist p*{
        replace missing =1 if missing(`var')
        }

10. Borrar o imputar los missings dependiendo cuántos sean. 

---------------------------------------------------------------------------------------------------------------------------

Este readme contiene información basada en la siguiente [liga](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/blob/master/temas/IV.optimizacion_convexa_y_machine_learning/4.1.Optimizacion_numerica_y_machine_learning.ipynb)

# Sobre los usos de la optimización numérica:
En la ciencia de datos se utilizan las aplicaciones desarrolladas en machine learning por ejemplo:

* Clasificación de documentos o textos: detección de spam.
* [Procesamiento de lenguaje natural](https://en.wikipedia.org/wiki/Natural_language_processing): named-entity recognition.
* [Reconocimiento de voz](https://en.wikipedia.org/wiki/Speech_recognition).
* [Visión por computadora](https://en.wikipedia.org/wiki/Computer_vision): reconocimiento de rostros o imágenes.
* Detección de fraude.
* [Reconocimiento de patrones](https://en.wikipedia.org/wiki/Pattern_recognition).
* Diagnóstico médico.
* [Sistemas de recomendación](https://en.wikipedia.org/wiki/Recommender_system).

Las aplicaciones anteriores involucran problemas como son:

* Clasificación.
* Regresión.
* Ranking.
* Clustering.
* Reducción de la dimensionalidad.


# Propuestas de bases de datos:
## Clasificación de documentos o textos: detección de spam.
* * [ ] [Kaggle: Sentiment140 dataset with 1.6 million tweets](https://www.kaggle.com/kazanova/sentiment140): It contains 1,600,000 tweets extracted using the twitter api . The tweets have been annotated (0 = negative, 4 = positive) and they can be used to detect sentiment. El dataset tiene una pequeña [ayuda](https://www.linkedin.com/pulse/social-machine-learning-h2o-twitter-python-marios-michailidis)
* * [ ] [Kaggle: Spam Text Message Classification](https://www.kaggle.com/team-ai/spam-text-message-classification): Let's battle with annoying spammer with data science.
* * [ ] [[Real or Fake] : Fake Job Description Prediction](https://www.kaggle.com/shivamb/real-or-fake-fake-jobposting-prediction): 18K job descriptions out of which about 800 are fake. 
* * [ ] [Text classification 20](https://www.kaggle.com/guiyihan/text-classification-20).
* * [ ] [BBC Full Text Document Classification](https://www.kaggle.com/shivamkushwaha/bbc-full-text-document-classification): 2225 documents in five categories can be used for clustering and classification.
* * [ ] [Tweet Sentiment Extraction](https://www.kaggle.com/c/tweet-sentiment-extraction): You're attempting to predict the word or phrase from the tweet that exemplifies the provided sentiment.

 
## Procesamiento de lenguaje natural: named-entity recognition.
* * [ ] [Kaggle: IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews): 50K movie reviews for natural language processing or Text analytics.
* * [ ] [Deep-NLP](https://www.kaggle.com/samdeeplearning/deepnlp)
  * Sheet1.csv contains 80 user responses, in the responsetext column, to a therapy chatbot. Bot said: 'Describe a time when you have acted as a resource for someone else'.  User responded. If a response is 'not flagged', the user can continue talking to the bot. If it is 'flagged', the user is referred to help.
  * Sheet2.csv contains 125 resumes, in the resumetext column. Resumes were queried from Indeed.com with keyword 'data scientist', location 'Vermont'. If a resume is 'not flagged', the applicant can submit a modified resume version at a later date. If it is 'flagged', the applicant is invited to interview.
* * [ ] [Text Similarity](https://www.kaggle.com/rishisankineni/text-similarity): **Train** - descriptionx, descriptiony, tickerx, tickery, samesecurity. **Test** - descriptionx, descriptiony, samesecurity(to be predicted)
* * [ ] [55000+ Song Lyrics](https://www.kaggle.com/mousehead/songlyrics): These are the lyrics for 57650 songs. They can be used for Natural Language Processing purposes, such as clustering of the words with similar meanings or predicting artist by the song. The dataset can be expanded with some more features for more advanced research like sentiment analysis. The data is not modified, only slightly cleaned, which gives a lot of freedom to devise your own applications.
* * [ ] [Python Questions from Stack Overflow](https://www.kaggle.com/stackoverflow/pythonquestions): Full text of all questions and answers from Stack Overflow that are tagged with the python tag. Useful for natural language processing and community analysis. See also the dataset of R questions.
* * [ ] [R Questions from Stack Overflow](https://www.kaggle.com/stackoverflow/rquestions): Full text of questions and answers from Stack Overflow that are tagged with the r tag, useful for natural language processing and community analysis.
* * [ ] [COVID-19 Open Research Dataset Challenge (CORD-19)](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge): a resource of over 52,000 scholarly articles, including over 41,000 with full text, about COVID-19, SARS-CoV-2, and related coronaviruses. This freely available dataset is provided to the global research community to apply recent advances in natural language processing and other AI techniques to generate new insights in support of the ongoing fight against this infectious disease.
* * [ ] [Hotel Reviews](https://www.kaggle.com/datafiniti/hotel-reviews): This is a list of 1,000 hotels and their reviews provided by Datafiniti's Business Database. The dataset includes hotel location, name, rating, review data, title, username, and more. **Posibilidad de obtener el data set completo.**
* * [ ] [State of the Union Corpus (1790 - 2018)](https://www.kaggle.com/rtatman/state-of-the-union-corpus-1989-2017): The State of the Union is an annual address by the President of the United States before a joint session of congress. In it, the President reviews the previous year and lays out his legislative agenda for the coming year.
* * [ ] [Stopword Lists for 19 Languages](https://www.kaggle.com/rtatman/stopword-lists-for-19-languages): This dataset is mainly helpful for use during NLP analysis, however there may some interesting insights to be found in the data.
* * [ ] [The Hunt for Prohibited Content](https://www.kaggle.com/c/avito-prohibited-content/data): Data for this competition consists mainly of Russian text. 
* * [ ] [Facebook Recruiting III - Keyword Extraction](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction)
* * [ ] [Sentiment Analysis on Movie Reviews](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews)
  
## Reconocimiento de voz.
* * [ ] [Gender Recognition by Voice](https://www.kaggle.com/primaryobjects/voicegender): This database was created to identify a voice as male or female, based upon acoustic properties of the voice and speech.**Mencionan SVM**
* * [ ] [Voice Recognition](https://www.kaggle.com/jeganathan/voice-recognition)
* * [ ] [Synthetic Speech Commands Dataset](https://www.kaggle.com/jbuchner/synthetic-speech-commands-dataset): We would like to have good open source speech recognition.
* * [ ] [Voice Recognition2](https://www.kaggle.com/rohankale/voice-recognition)
* * [ ] [Alexa Dataset](https://www.kaggle.com/aanhari/alexa-dataset): Voice-first applications need a wake-word to start listening to your commands. The Alexa dataset contains recordings of Alexa keyword that can be used for building the voice-first experience.
* * [ ] [Speaker_recognition](https://www.kaggle.com/analystanand/speaker-recognition): Identify speaker voice irrespective of speech what they are speaking.

## Visión por computadora: reconocimiento de rostros o imágenes.
* * [ ] [Horses Or Humans Dataset](https://www.kaggle.com/sanikamal/horses-or-humans-dataset):Horses or Humans is a dataset of 300×300 images, created by Laurence Moroney, that is licensed CC-By-2.0 for anybody to use in learning or testing computer vision algorithms.
* * [ ] [Stanford Dogs Dataset](https://www.kaggle.com/jessicali9530/stanford-dogs-dataset): Over 20,000 images of 120 dog breeds
* * [ ] [Basket Ball Computer Vision](https://www.kaggle.com/chrisparker126/basket-ball-computer-vision): I'm interested in object recognition, and trying to learn how to build CNN models able to recognize specific objects.
* * [ ] [Sign Language MNIST](https://www.kaggle.com/datamunge/sign-language-mnist): Drop-In Replacement for MNIST for Hand Gesture Recognition Tasks
* * [ ] [Keras Pretrained models](https://www.kaggle.com/gaborfodor/keras-pretrained-models): Kaggle has more and more computer vision challenges. Although Kernel resources were increased recently we still can not train useful CNNs without GPU. The other main problem is that Kernels can't use network connection to download pretrained keras model weights. This dataset helps you to apply your favorite pretrained model in the Kaggle Kernel environment.
* * [ ] [Rock Paper Scissors Dataset](https://www.kaggle.com/sanikamal/rock-paper-scissors-dataset): Rock Paper Scissors – A multi class dataset for learning computer vision
* * [ ] [Passenger Screening Algorithm Challenge](https://www.kaggle.com/c/passenger-screening-algorithm-challenge): This dataset contains a large number of body scans acquired by a new generation of millimeter wave scanner called the High Definition-Advanced Imaging Technology (HD-AIT) system. The competition task is to predict the probability that a given body zone (out of 17 total body zones) has a threat present.
* * [ ] [Carvana Image Masking Challenge](https://www.kaggle.com/c/carvana-image-masking-challenge): large number of car images (as .jpg files). Each car has exactly 16 images, each one taken at different angles.


## Detección de fraude.
* * [ ] [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud): transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. 
* * [ ] [TalkingData AdTracking Fraud Detection Challenge](https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection)
* * [ ] [HEALTHCARE PROVIDER FRAUD DETECTION ANALYSIS](https://www.kaggle.com/rohitrox/healthcare-provider-fraud-detection-analysis): The goal of this project is to " predict the potentially fraudulent providers " based on the claims filed by them.along with this, we will also discover important variables helpful in detecting the behaviour of potentially fraud providers. 
* * [ ] [Credit card fraud detection](https://www.kaggle.com/dileep070/anomaly-detection): Python notebook using data from Credit Card Fraud Detection.



## Reconocimiento de patrones.
datasets repetidos


## Diagnóstico médico.
* * [ ] [revisar](https://www.kaggle.com/search?q=Medical+Diagnosis+in%3Adatasets)



## Sistemas de recomendación.
* * [ ] [Santander Product Recomendation](https://www.kaggle.com/marialuiza07/santander-product-recomendation)
* * [ ] [S product recomendation](https://www.kaggle.com/silviosantana/s-product-recomendation)
* * [ ] [YahooMusic](https://www.kaggle.com/c/ee627A-Spring2019)
* * [ ] [Movie recomendation TS Spring 2020](https://www.kaggle.com/c/movie-recomendation-ts-spring-2020): **Está en ruso :(**
* * [ ] [datasets](https://www.kdnuggets.com/2016/02/nine-datasets-investigating-recommender-systems.html)
* * [ ] [More Datasets](https://cseweb.ucsd.edu/~jmcauley/datasets.html)
* * [ ] [Netflix Prize data](https://www.kaggle.com/netflix-inc/netflix-prize-data)
* * [ ] [Spotify](https://research.spotify.com/datasets)
* * [ ] [Anime Recommendations Database](https://www.kaggle.com/CooperUnion/anime-recommendations-database): 73,516 users on 12,294 anime. 
* * [ ] [Springleaf Marketing Response](https://www.kaggle.com/c/springleaf-marketing-response): You are provided a high-dimensional dataset of anonymized customer information. Each row corresponds to one customer. The response variable is binary and labeled "target". You must predict the target variable for every row in the test set.
* * [ ] [Santander Product Recommendation](https://www.kaggle.com/c/santander-product-recommendation)
* * [ ] [Elo Merchant Category Recommendation](https://www.kaggle.com/c/elo-merchant-category-recommendation)
* * [ ] [Expedia Hotel Recommendations](https://www.kaggle.com/c/expedia-hotel-recommendations): Expedia has provided you logs of customer behavior. These include what customers searched for, how they interacted with search results (click/book), whether or not the search result was a travel package. The data in this competition is a random selection from Expedia and is not representative of the overall statistics.
* * [ ] [Crowdflower Search Results Relevance](https://www.kaggle.com/c/crowdflower-search-relevance)
* * [ ] [Personalized Web Search Challenge](https://www.kaggle.com/c/yandex-personalized-web-search-challenge)

## Otros...
* * [ ] [Santander Customer Satisfaction](https://www.kaggle.com/c/santander-customer-satisfaction)
* * [ ] [Acquire Valued Shoppers Challenge](https://www.kaggle.com/c/acquire-valued-shoppers-challenge)
* * [ ] [Personalize Expedia Hotel Searches - ICDM 2013](https://www.kaggle.com/c/expedia-personalized-sort)
* * [ ] [Outbrain Click Prediction](https://www.kaggle.com/c/outbrain-click-prediction)
* * [ ] [Click-Through Rate Prediction](https://www.kaggle.com/c/avazu-ctr-prediction)
* * [ ] [Influencers in Social Networks](https://www.kaggle.com/c/predict-who-is-more-influential-in-a-social-network)
* * [ ] [Walmart Recruiting II: Sales in Stormy Weather](https://www.kaggle.com/c/walmart-recruiting-sales-in-stormy-weather)






