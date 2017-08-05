# Implementation of model1 from main notebook

from nltk.corpus import stopwords
from nltk import word_tokenize

texted = input("Enter the test sentence ")

stop_words = set(stopwords.words('english'))
token = word_tokenize(texted)

filtered_sentence = [w for w in token if not w in stop_words]

filtered_sentence = []

for w in token:
    if w not in stop_words:
        filtered_sentence.append(w)

# the initials lists
happy = []
sad = []
anger = []
disgust = []
fear = []
surprise = []

# flags
happy_flag = 0
sad_flag = 0
anger_flag = 0
disgust_flag = 0
fear_flag = 0
surprise_flag = 0

# searching elements of filtered_sentence in lists and increasing respective flag

for key in filtered_sentence:
    if key in happy is True:
        happy_flag = happy_flag + 1
    elif key in sad is True:
        sad_flag = sad_flag + 1
    elif key in happy is True:
        anger_flag = anger_flag + 1
    elif key in happy is True:
        disgust_flag = disgust_flag + 1
    elif key in happy is True:
        fear_flag = fear_flag + 1
    elif key in happy is True:
        surprise_flag = surprise_flag + 1
    else:
        pass


def TypeOfSentence(happy_flag, sad_flag, anger_flag, disgust_flag, fear_flag, surprise_flag):
    return max(happy_flag, sad_flag, anger_flag, disgust_flag, fear_flag, surprise_flag)


print(TypeOfSentence())
