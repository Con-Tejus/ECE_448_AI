# viterbi.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Renxuan Wang (renxuan2@illinois.edu) on 10/18/2018

"""
This is the main entry point for MP5. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""

'''
TODO: implement the baseline algorithm.
input:  training data (list of sentences, with tags on the words)
        test data (list of sentences, no tags on the words)
output: list of sentences, each sentence is a list of (word,tag) pairs. 
        E.g., [[(word1, tag1), (word2, tag2)], [(word3, tag3), (word4, tag4)]]
'''
def baseline(train, test):
    predicts = []
    type = {}
    type['DET'] = {}
    type['NOUN'] = {}
    type['VERB'] = {}
    type['ADJ'] = {}
    type['ADP'] = {}
    type['.'] = {}
    type['ADV'] = {}
    type['CONJ'] = {}
    type['PRT'] = {}
    type['PRON'] = {}
    type['NUM'] = {}
    type['X'] = {}
    type_list = ['DET','NOUN','VERB','ADJ','ADP','.', 'ADV', 'CONJ', 'PRT','PRON','NUM','X']
    # j[1] gives the type of the word
    # j[0] gives the word
    type_check = 0
    word_type = ''
    sentence_list = []
    
    for i in train:
        for j in i:
            if type[j[1]].get(j[0],0) == 0:
                type[j[1]][j[0]] = 1
            else:
                type[j[1]][j[0]] = 1 + type[j[1]][j[0]]
            
    #test[i] gives the sentence
    #test[i][j] gives the word
    for count,sentence in enumerate(test):
        sentence_list = []
        for word in sentence:
            type_check = 0
            for j in type_list:
                if (type[j].get(word,0) > type_check):
                    word_type = j
                    type_check = type[j].get(word,0)
            word_out = (word,word_type)
            sentence_list.append(word_out)
        predicts.append(sentence_list)

    return predicts

'''
TODO: implement the Viterbi algorithm.
input:  training data (list of sentences, with tags on the words)
        test data (list of sentences, no tags on the words)
output: list of sentences with tags on the words
        E.g., [[(word1, tag1), (word2, tag2)], [(word3, tag3), (word4, tag4)]]
'''
def viterbi(train, test):
    predicts = []
    type = {}
    type['DET'] = {}
    type['NOUN'] = {}
    type['VERB'] = {}
    type['ADJ'] = {}
    type['ADP'] = {}
    type['.'] = {}
    type['ADV'] = {}
    type['CONJ'] = {}
    type['PRT'] = {}
    type['PRON'] = {}
    type['NUM'] = {}
    type['X'] = {}
    type_list = ['DET','NOUN','VERB','ADJ','ADP','.', 'ADV', 'CONJ', 'PRT','PRON','NUM','X']
    # j[1] gives the type of the word
    # j[0] gives the word
    type_check = 0
    word_type = ''
    sentence_list = []
    
    initialCount = 0
    transitionCount = 0
    emissionCount = 0


   
    #Initial probability: check first tag of each sentence
    #Transition probability: while going through sentence, keep copy of current tag, move to next one 
    
    

    return predicts
