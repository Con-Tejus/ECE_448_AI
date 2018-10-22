from math import log
# naive_bayes.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Justin Lizama (jlizama2@illinois.edu) on 09/28/2018

"""
This is the main entry point for MP4. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
#P(word | spam) = P(word and spam)/P(spam)
def naiveBayes(train_set, train_labels, dev_set, smoothing_parameter):

    #p_S is already .50 due to training set
    p_S = .50
    p_H = .50
    dev_emails = []
    trainHam = {}
    trainSpam = {}
    spamTotal = 0
    hamTotal = 0

    for idx,email in enumerate(train_set):
        for word in email:
            if train_labels[idx] == 1:
                trainSpam[word] = trainSpam.get(word, 0) + 1
                spamTotal += 1
            else:
                trainHam[word] = trainHam.get(word, 0) + 1
                hamTotal += 1

    def conditionalWord(word, spam,numWords):
        if spam:
            return (trainSpam.get(word,0)+smoothing_parameter)/(float)(spamTotal+smoothing_parameter*numWords)
        return (trainHam.get(word,0)+smoothing_parameter)/(float)(hamTotal+smoothing_parameter*numWords)

    #gives the conditional probability p(B | A_x)
    #only for one email
    def conditionalEmail(body, spam):
        result = 0
        numWords = len(body)
        for word in body:
            result += log(conditionalWord(word, spam,numWords))
        return result

    for email in dev_set:
        isSpam = p_S * conditionalEmail(email, True) # P (A | B)
        notSpam = p_H * conditionalEmail(email, False) # P(¬A | B)
        if (isSpam > notSpam):
            dev_emails.append(1)
        else:
            dev_emails.append(0)
    
    print(dev_emails)

    return dev_emails
    
