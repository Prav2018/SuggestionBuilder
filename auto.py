# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:15:55 2018

@author: Prav
"""
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
from pickle import dump
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding

#
#import pylab as pl
#
#print(lin_thesaurus.fileids())
#sentences_twitter = twitter_samples.strings('tweets.20150430-223406.json')
#print(len(twitter_samples.strings('tweets.20150430-223406.json')))
import cleaner

# sentences =["Does John have any HLI high confidence regions variants EOS",
#             "Is there a MYH7 variants in John's sample EOS",
#             "Are there any ACMG 59 genes variants in John's sample EOS",
#             "Does John have any stopgain variants EOS",
#             "Does John have any homozygous variants EOS",
#             "Does John have any variants that have CADD score >=15 EOS",
#             "Does John have any loss-of-function variants EOS",
#             "Does John have any protein alternating variants EOS",
#             "Does John have any variants associated with Parkinson's disease EOS",
#             "Does John have any genes associated with Parkinson's disease EOS",
#             "What are the chances of getting trails approved EOS",
#             "How many percentage of people are suffering from flu in california EOS",
#             "When does the chances of getting approved improves EOS"]
# # # # sentences_own = ["What are the important topics for the exam .",
# # # #                  "I am taking leave tomorrow .",
# # # #                  "Who got the visa .",
# # # #                  "What is your favorite color .",
# # # #                  "Happy birthday to you .",
# # # #                  "Thank you for your cooperation .",
# # # #                  "May I know your name ."]
# # # #sentences_own = " ".join(sentences)
# # #
# # # sentences_own=["".join(cleaner.clean_doc(line)) for line in sentences]
# # # #
# # # #sentences_own = ["What are the important topics for the exam",
# # # #                 "I am taking leave tomorrow"]
# # #
# # #
# import SentenceBuilder as sb
#
# sentences_own=sb.sentences
# for sent in sentences:
#     sentences_own.append(sent)
# tokenizer = Tokenizer(lower= True, split=' ')
# tokenizer.fit_on_texts(sentences_own)
# vocab_size = tokenizer.texts_to_sequences(["does john have"])[0]
# cc = tokenizer.word_docs
#

# # ## print(tokenizer.word_index)
# # ##
# # ##
# # ##
# # ##
# sequences =[]
# for line in sentences_own:
#    encoded = tokenizer.texts_to_sequences([line])[0]
#    for i in range(1, len(encoded)):
#        seq= encoded[:i+1]
#        sequences.append(seq)
#
# max_seq_len = max([len(seq)for seq in sequences])
# sequences = pad_sequences(sequences, maxlen= max_seq_len, padding='pre')
# #sequences = np.array(sequences)
# #import numpy as np
# #sequences = np.array(sequences)
# X, y = sequences[:,:-1], sequences[:,-1]
# # #from sklearn import preprocessing
# # #X = preprocessing.normalize(X)
# y = to_categorical(y, num_classes= vocab_size)
#
# model = Sequential()
# model.add(Embedding(vocab_size, 32, input_length=max_seq_len-1))
# model.add(LSTM(80, return_sequences= True))
# model.add(LSTM(100))
# model.add(Dense(100, activation='relu'))
# model.add(Dense(vocab_size, activation='softmax'))
# print(model.summary())
# # # compile model
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# # # fit model
# model.fit(X, y, batch_size=4, epochs=100, verbose=1)
#
# ## save the model to file
# model.save('model.h5')
# ## save the tokenizer
# dump(tokenizer, open('tokenizer.pkl', 'wb'))
# dump(max_seq_len, open('max_seq_len.pkl', 'wb'))



##Testing##
from keras.models import load_model
from pickle import load
#import re
model = load_model('model.h5')
global graph
import tensorflow as tf
graph = tf.get_default_graph()
tokenizer = load(open('tokenizer.pkl', 'rb'))
max_seq_len = load(open('max_seq_len.pkl', 'rb'))
max_sentences = 8
from multiprocessing import Process
threads=[]
import numpy as np
def run(text):
    res=buildSentence(model, tokenizer, "".join(cleaner.clean_doc(text)))
    print(res)
    return res

def buildSentence(model, tokenizer, text):
    sentences = [ ]
    encoded = encodeWords(tokenizer,text)
    with graph.as_default():
        pred = model.predict_proba(encoded, verbose=0)
        # preds = np.argsort(pred[0])[-max_sentences:]

        preds = [index for index,label in enumerate(pred[0]) if label>=0.0009]
        for i in preds:
            word = getWord(tokenizer,i)
            if word!= "eos":
                sentences.append(predictSentence(text,word))

    return sentences


def predictSentence(prime,next_word):
    output=[]
    output.append(prime)
    output.append(next_word)
    encoded = encodeWords(tokenizer," ".join(output))
    with graph.as_default():
        i = 0
        while True:
#            print(text)
            pred = model.predict_classes(encoded, verbose=0)
            # probb = model.predict_proba(encoded)
            # print(max(model.predict_proba(encoded)))
            word = getWord(tokenizer,pred)
            if word == 'eos':
                break
            output.append(word)
            text = " ".join(output)
            encoded = encodeWords(tokenizer,text)
            i+=1
    return " ".join(output)


def encodeWords(tokenizer,text):
    word="".join(cleaner.clean_doc(text))
    seq=tokenizer.texts_to_sequences([word])[0]
    encoded = pad_sequences([seq], maxlen= max_seq_len-1, padding='pre')
    return encoded

def getWord(tokenizer,pred):
    res=""
    for word, index in tokenizer.word_index.items():
        if index == pred:
            res=word
            break
    return res

# text="does mark have any"
# run(text)

