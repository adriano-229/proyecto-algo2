import copy
import math
import os
import re

import PyPDF2

import word_class as wc


def pdf2str(path, file):
    with open(os.path.join(path, file), 'rb') as f:
        reader = PyPDF2.PdfReader(f)

        txt = ""
        for p in range(len(reader.pages)):
            txt += reader.pages[p].extract_text()
    return txt


def str2words(txt):
    words = []
    for s in txt:
        words.append(s.split(' '))
    return words


def separate(term):
    low = term.lower()
    sep = re.findall(r'[a-zA-ZñÑáéíóúÁÉÍÓÚ]+|\d+', low)
    return sep


def create_word_list(string):
    word_list = []

    terms = string.split(' ')
    for term in terms:
        words = separate(term)
        for word in words:
            word = wc.clean(word)
            if word:
                word_list.append(word)
    return word_list


def create_dicc(dicc, lst):
    for e in lst:
        if e not in dicc:
            dicc[e] = .0
    return dicc


def create(path):
    if not os.path.isdir(path):
        quit("The provided path is not a directory")

    pdfs_str = []
    corpus = os.listdir(path)

    for file in corpus:
        pdf_s = pdf2str(path, file)
        pdfs_str.append(pdf_s)

    word_lists = []
    for pdf_s in pdfs_str:
        word_list = create_word_list(pdf_s)
        word_lists.append(word_list)

    general_hash = {}
    for word_list in word_lists:
        general_hash = create_dicc(general_hash, word_list)

    tf_list = []
    for word_list in word_lists:
        tf = copy.deepcopy(general_hash)
        for word in word_list:
            tf[word] += 1
        for word in tf.keys():
            count = tf[word]
            if count != 0:
                _tf = count / len(word_list)
                tf[word] = _tf
        tf_list.append(tf)

    idf = copy.deepcopy(general_hash)
    for tf in tf_list:
        for word, tfreq in tf.items():
            if tfreq > 0:
                idf[word] += 1
        for word, _idf in idf.items():
            if _idf != 0:
                idf[word] = math.log2(len(corpus) / _idf)
            else:
                idf[word] = 0

    tfidf_vectors_list = []
    for tf in tf_list:
        tfidf_vector = {}
        for word in tf.keys():
            tfidf_vector[word] = tf[word] * idf[word]
        tfidf_vectors_list.append(tfidf_vector)

    for vec in tfidf_vectors_list:
        for w, ti in vec.items():
            print(w, ti)
        print()

    # todo PICKLE DE LOS VECTORES, ENCAPSULAR FUNCIONES Y EMPEZAR EL SEARCH


if __name__ == "__main__":
    create(
        "/home/admin1/Documents/Universidad/2do/Algoritmos 2/proyecto-algo2/code/test_pdfs")  # poner el dir adecuado
