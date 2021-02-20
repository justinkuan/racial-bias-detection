import os
import numpy as np
import pandas as pd
from pprint import pprint
import re
import pickle
import spacy
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Parameters from grid-searching
ALPHA = 'asymmetric'
ETA = 1
NTOPICS = 14

# Add a few more stopwords
stop_words = stopwords.words('english')
stop_words.extend(['reuters', 'say', 's'])

def sent_to_words(sentences):
    '''Function returns words from sentences'''
    for sentence in sentences:
        yield(simple_preprocess(str(sentence), deacc=True))  # True removes punctuations

def remove_failed_encoding(string):
    '''Preprocessing script on a given string'''
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

def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """https://spacy.io/api/annotation"""
    nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent)) 
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out

def preprocess_text(string):
    '''Function performs a series of text preprocessing'''
    string = remove_failed_encoding(string)
    string = remove_punctuation(string)
    string = convert_to_lowercase(string)
    return string

def make_corpus(df):
    '''Function returns elements of topic modeling from a dataset'''
    data_words = list(sent_to_words(df))
    data_words_nostops = remove_stopwords(data_words)
    data_words_nostops = remove_stopwords(data_words_nostops)
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

def build_lda_model(corpus, id2word, n_topics, alpha, eta):
    lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=n_topics, 
                                           random_state=100,
                                           chunksize=100,
                                           passes=10,
                                           alpha=alpha,
                                           eta=eta)
    # pprint(lda_model.print_topics(n_topics))
    return lda_model

def find_best_matching_topic(lda_model, n_topics=NTOPICS):
    '''Function returns the topic number (int), with most matching word to keywords, i.e.,
       ['black', 'police', 'violence', 'kill', 'arrest']
    '''
    racial_violence = ['black', 'police', 'violence', 'kill', 'arrest']
    topic_map = {}  # {topic_nth: sum of matching words}

    for n,index in enumerate(range(n_topics)):    
        for tup in lda_model.show_topic(n, topn=n_topics+10):
            topic_word = tup[0]
            if topic_word in racial_violence:
                topic = index
                if topic not in topic_map.keys():
                    topic_map[topic] = 1
                else:
                    topic_map[topic] +=1
    try:                
        best_topic_no, quantity = sorted(topic_map.items(), key = lambda tup: tup[1], reverse=True)[0]
        print('Topic {topic: total keywords}-candidates are :', topic_map)
        print('Best matching topic number is:', best_topic_no )
        return best_topic_no if quantity != 1 else 99 
    except IndexError:
        print('no matching topic number')
        return 99

def model_first_batch():
    filename = "subset_first_15000"
    filepath = os.path.join('data', 'interim', f'{filename}.gzip')
    msg = f'{filename}.gzip doesnt exist in data/interim folder'
    assert os.path.exists(filepath), msg
    
    # Import file
    df = pd.read_parquet(filepath, engine="pyarrow")
    # Preprocess 
    papers = df['article'].apply(preprocess_text)
    # Prepare topic modeling input
    corpus, id2word, bigrams, data_lemmatized = make_corpus(papers)
    # Build model & print the topic number with best matching keywords
    lda_model = build_lda_model(corpus, id2word, n_topics=NTOPICS, alpha=ALPHA, eta=ETA)
    best_topic_no = find_best_matching_topic(lda_model, n_topics=NTOPICS)
    # label document
    df['topic'] = extract_labels(lda_model, data_lemmatized, corpus, n_topics=NTOPICS)
    print(f'Topic {best_topic_no} has ', df[df.topic==best_topic_no].shape[0], ' rows')
    # Save file & model
    filepath = os.path.join('data', 'interim', f'labeled_{filename}.gzip')
    df.to_parquet(filepath, compression='gzip')
    with open(f"models/lda_model_n{NTOPICS}_first15000.pkl", "wb") as fout:
        pickle.dump(lda_model, fout)
        print(f'LDA model saved as models/lda_model_n{NTOPICS}_first15000.pkl')

def main():
    model_first_batch()
    
if __name__=="__main__":
    main()
    print("Data labeling complete!")
