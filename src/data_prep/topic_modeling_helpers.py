import numpy as np
import re
import spacy
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords

# Add a few more stopwords
stop_words = stopwords.words('english')
stop_words.extend(['reuters', 'say','s'])

def sent_to_words(sentences):
    for sentence in sentences:
        yield(simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

def remove_failed_encoding(string):
    string = re.sub("â€”",'',string)    
    string = re.sub("â€™",'',string)
    string = re.sub("â€œ",'',string)
    string = re.sub("â€¦",'',string)    
    string = re.sub("Â",'',string)
    string = re.sub("\xa0",' ',string)
    string = re.sub("\'","'",string)
    return string

def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

def remove_punctuation(string):
    return re.sub(r'[^\w\s]', '', string)

def convert_to_lowercase(string):
    return string.lower()

def make_bigrams(data_words):
    bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100) # higher thresh fewer phrases.
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    return [bigram_mod[doc] for doc in data_words]

def make_trigrams(data_words):
    trigram = gensim.models.Phrases(bigram[data_words], threshold=100)
    trigram_mod = gensim.models.phrases.Phraser(trigram)
    return [trigram_mod[bigram_mod[doc]] for doc in data_words]

def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """https://spacy.io/api/annotation"""
    nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent)) 
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out

def preprocess_text(string):
    string = remove_failed_encoding(string)
    string = remove_punctuation(string)
    string = convert_to_lowercase(string)
    return string

def make_corpus(df):
    data_words = list(sent_to_words(df))
    data_words_nostops = remove_stopwords(data_words)
    data_words_nostops = remove_stopwords(data_words)
    data_words_nostops = remove_stopwords(data_words)
    bigrams = make_bigrams(data_words_nostops)
    data_lemmatized = lemmatization(bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
    
    id2word = corpora.Dictionary(data_lemmatized)
    id2word.filter_extremes(no_below=10, no_above=0.45)
    id2word.compactify()
    
    corpus = [id2word.doc2bow(data) for data in data_lemmatized]
    return corpus, id2word, bigrams, data_lemmatized

def extract_labels(lda_model, data, corpus, n_topics):
    labels = []
    for i in range(len(data)):
        top_topics = lda_model.get_document_topics(corpus[i], minimum_probability=0.0)
        topic_vec = [top_topics[i][1] for i in range(n_topics)]
        labels.append(np.argmax(topic_vec))
    return labels
