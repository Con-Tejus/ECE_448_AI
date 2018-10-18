import math
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
    spam_count = 0
    count = 0
    count_dict = {}
    word_set = set()
    word_count = 0
    for idx, email in enumerate(train_set):
        if train_labels[idx] == 1:
            spam_count += 1
        for word in email:
            if train_labels[idx] == 1:
                try:
                    spam_dict[word] += 1
                except KeyError:
                    spam_dict[word] = 1
            word_set.add(word)
            word_count += 1
        count += 1
    pSpam = spam_count/count
    ham_dict = {}
    for k,v in spam_dict.items():
        spam_dict[k] = (v/(word_count))
        ham_dict[k] = log(1) / log(v/word_count)
        print(v/word_count)
        # word_count += 1

    pUNK = smoothing_parameter/(word_count+1+len(word_set))
    ham_sum = 0
    spam_sum = 0
    # for idx, email in enumerate(train_set):
    #     sum = 0
    #     for word in email:
    #         try:
    #             sum += math.log(spam_dict[word])
    #         except KeyError:
    #             sum += math.log(pUNK)
    #     if train_labels[idx] == 1:
    #         spam_sum += sum
    #     else:
    #         ham_sum += sum
    # avg_spam_sum = spam_sum/spam_count
    # avg_ham_sum = ham_sum/(count-spam_count)

    output = []
    for email in dev_set:
        spam_sum = 0
        ham_sum = 0
        for word in email:
            try:
                spam_sum += math.log(spam_dict[word])
                # print(word,spam_dict[word])
                ham_sum += math.log(1-spam_dict[word])
            except KeyError:
                spam_sum += math.log(pUNK)
                ham_sum += math.log(1-pUNK)
        # print(sum)
        # if abs(sum-avg_ham_sum) > abs(sum-avg_spam_sum):
        #     output.append(1)
        # else:
        #     output.append(0)
        if spam_sum > ham_sum:
            output.append(1)
        else:
            output.append(0)
    print(output)
    return output

    """
    train_set - List of list of words corresponding with each email
    example: suppose I had two emails 'i like pie' and 'i like cake' in my training set
    Then train_set := [['i','like','pie'], ['i','like','cake']]

    train_labels - List of labels corresponding with train_set
    example: Suppose I had two emails, first one was spam and second one was ham.
    Then train_labels := [1,0]

    dev_set - List of list of words corresponding with each email that we are testing on
              It follows the same format as train_set

    smoothing_parameter - The smoothing parameter you provided with --laplace (1.0 by default)
    """
    # TODO: Write your code here
    # return predicted labels of development set
    return []
