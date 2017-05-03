"""
Minimum Viable Product Magic 8 Ball

Very simple, takes user input question, and returns a random answer from the set
of 20 standard Magic 8 Ball responses.

"""
from isquestion import isQuestion
from isynquestion import isYesNoQuestion
import random
import indicoio
import operator
indicoio.config.api_key = 'f954e20684d172b9ebcc869bc9fac4b1'
from google.cloud import language
language_client = language.Client()

def wordForm(sorted_keywords):
    document = language_client.document_from_text(sorted_keywords)
    annotations = document.annotate_text().tokens
    words = {}
    for token in annotations:
        word = token.text_content
        pos = token.part_of_speech
        words[word] = pos
    return words


wh_words = ["who", "what", "when", "where", "which", "who", "whom", "whose", "why", "how"]
yn_words = ["can", "could", "may", "might", "shall", "should", "will", "would", "must", "ought", "be", "do", "have"]
question_words = wh_words + yn_words

default_positive = ['It is certain', 'It is decidedly so', 'Without a doubt',
'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
'Yes', 'Signs point to yes']

default_neutral = ['Reply hazy, try again', 'Ask again later', 'Better not to tell you now',
'Cannot predict now', 'Concentrate and ask again']

default_negative = ['Don\'t count on it', 'My reply is no', 'My sources say no',
'Outlook not so good', 'Very doubtful']

defaults = default_positive + default_neutral + default_negative

con = True
while (con):
    user_input = input('Ask any question you would like to ask the Magic 8 Ball: ')
    keywords = indicoio.keywords(user_input, top_n = 5)
    for k in list(keywords.keys()):
        s = k.split(" ")
        if len(s) > 1:
            del(keywords[k])
    sorted_keywords = sorted(keywords.items(), key = operator.itemgetter(1), reverse = True)
    sorted_keywords_keys = []
    for i in range(0,len(sorted_keywords)):
        sorted_keywords_keys.append(sorted_keywords[i][0])
    sorted_keywords_keys = " ".join(str(s) for s in sorted_keywords_keys)
    document = language_client.document_from_text(sorted_keywords_keys)
    annotations = document.annotate_text().tokens
    wordForms = wordForm(sorted_keywords_keys)
    for token in wordForms:
        if wordForms[token] == "VERB":
            print(wordForms[token])

    if isQuestion(user_input, question_words):
        if isYesNoQuestion(user_input, yn_words):
            random_answer = random.randint(0,19)
            print(defaults[random_answer])
        else:
            print("That's not a yes or no question, so I'm not sure.")
            print("But I think you should ")
    else:
        print("That's not a question. I think.")
