# Given two sentences, return an array that has the words that appear in one sentence and not
# the other and an array with the words in common.

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'


def solution(sent1, sent2):
    commons = set([x for x in (sent1 + ' ' + sent2).split(' ')
                   if x in sent2.split(' ') and x in sent1.split(' ')])
    diffs1 = [x for x in (sent1 + ' ' + sent2).split(' ')
              if x in sent1.split(' ') and x not in sent2.split(' ')]
    diffs2 = [x for x in (sent1 + ' ' + sent2).split(' ')
              if x in sent2.split(' ') and x not in sent1.split(' ')]

    # set1 = set(sent1.split(' '))
    # set2 = set(sent2.split(' '))
    # print(set1 ^ set2)
    # print(set1 & set2)
    print(f'commons-> {commons}')
    print(f'diffs-> {set(diffs1 + diffs2)}')

# ^ A.symmetric_difference(B), & A.intersection(B)


solution(sentence1, sentence2)
