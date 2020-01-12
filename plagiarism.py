from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
from gensim import corpora, models, similarities
import numpy as np
import os
import glob
from pdf2text import pdf2text


def OneToMany(file1,dir,i):
    ps = PorterStemmer()
    file_docs = []
    tokens = sent_tokenize(pdf2text(file1))
    for line in tokens:
        file_docs.append(line)
    for line in file_docs:
        words = [w.lower() for w in word_tokenize(line)]
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in words]
        words = [word for word in stripped if word.isalpha()]
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
        words = [ps.stem(words) for words in words]
        words = [d.split() for d in words]
        dictionary = corpora.Dictionary(words)
        corpus = [dictionary.doc2bow(words) for words in words]
        tf_idf = models.TfidfModel(corpus)
        sims = similarities.Similarity('workdir/', tf_idf[corpus], num_features=len(dictionary))


    file2_docs = []
    file2 = sorted(glob.iglob(os.path.join(dir, '*.pdf')), key=os.path.getctime)

    tokens = sent_tokenize(pdf2text(file2[i]))
    for line in tokens:
        file2_docs.append(line)
    avg_sims = []
    for line in file2_docs:
        words2 = [w.lower() for w in word_tokenize(line)]
        table2 = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table2) for w in words2]
        words2 = [word for word in stripped if word.isalpha()]
        stop_words = set(stopwords.words('english'))
        words2 = [w for w in words2 if not w in stop_words]
        words2 = [ps.stem(words2) for words2 in words2]
        query_doc_bow = dictionary.doc2bow(words2)
        query_doc_tf_idf = tf_idf[query_doc_bow]
        sum_of_sims = (np.sum(sims[query_doc_tf_idf], dtype=np.float32))
        avg = sum_of_sims / len(file_docs)
        avg_sims.append(avg)

    total_avg = np.sum(avg_sims, dtype=np.float)
    percentage_of_similarity = round(float(total_avg) * 100)
    if percentage_of_similarity >= 100:
        percentage_of_similarity = 100
    x = os.path.basename(file1)
    y = os.path.basename(file2[i])

    print("SIMILARITY BETWEEN "+ x +" AND "+ y +": {}%".format(percentage_of_similarity))





def OneToOne(file1,file2):
    ps = PorterStemmer()
    file_docs = []
    tokens = sent_tokenize(pdf2text(file1))
    for line in tokens:
        file_docs.append(line)
    for line in file_docs:
        words = [w.lower() for w in word_tokenize(line)]
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in words]
        words = [word for word in stripped if word.isalpha()]
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
        words = [ps.stem(words) for words in words]
        words = [d.split() for d in words]
        dictionary = corpora.Dictionary(words)
        corpus = [dictionary.doc2bow(words) for words in words]
        tf_idf = models.TfidfModel(corpus)
        sims = similarities.Similarity('workdir/', tf_idf[corpus], num_features=len(dictionary))



    file2_docs = []
    tokens = sent_tokenize(pdf2text(file2))

    avg_sims = []
    for line in tokens:
        file2_docs.append(line)
        for line in file2_docs:
            query_token = [w.lower() for w in word_tokenize(line)]
            table2 = str.maketrans('', '', string.punctuation)
            stripped = [w.translate(table2) for w in query_token]
            words2 = [word for word in stripped if word.isalpha()]
            stop_words = set(stopwords.words('english'))
            words2 = [w for w in words2 if not w in stop_words]
            words2 = [ps.stem(words2) for words2 in words2]
            query_doc_bow = dictionary.doc2bow(words2)
            query_doc_tf_idf = tf_idf[query_doc_bow]
            sum_of_sims = (np.sum(sims[query_doc_tf_idf], dtype=np.float32))
            avg = sum_of_sims / len(file_docs)
            avg_sims.append(avg)


    total_avg = np.sum(avg_sims, dtype=np.float)
    percentage_of_similarity = round(float(total_avg) * 100)
    if percentage_of_similarity >= 100:
        percentage_of_similarity = 100
    x = os.path.basename(file1)
    y = os.path.basename(file2)

    print("SIMILARITY BETWEEN " + x + " AND " + y + ": {}%".format(percentage_of_similarity))






