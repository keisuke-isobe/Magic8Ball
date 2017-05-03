"""
Minimum Viable Product Magic 8 Ball

Very simple, takes user input question, and returns a random answer from the set
of 20 standard Magic 8 Ball responses.

"""
from isquestion import isQuestion
from isynquestion import isYesNoQuestion
import random
import indicoio
indicoio.config.api_key = 'f954e20684d172b9ebcc869bc9fac4b1'
from google.cloud import language
language_client = language.Client()

text = "Who stole my bike?"
document = language_client.document_from_text(text)

wh_words = ["who", "what", "when", "where", "which", "who", "whom", "whose", "why", "how"]
yn_words = ["can", "could", "may", "might", "shall", "should", "will", "would", "must", "ought", "be", "do", "have"]
question_words = wh_words + yn_words
print(isQuestion(text, question_words))
print(isYesNoQuestion(text, yn_words))
keywords = indicoio.keywords(text, top_n = 4))
print(vars(keywords))
print(keywords)

annotations = document.annotate_text().tokens
print(type(annotations))
for token in annotations:
    print(token.part_of_speech, token.text_content)

default_positive = ['It is certain', 'It is decidedly so', 'Without a doubt',
'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
'Yes', 'Signs point to yes']

default_neutral = ['Reply hazy, try again', 'Ask again later', 'Better not to tell you now',
'Cannot predict now', 'Concentrate and ask again']

default_negative = ['Don\'t count on it', 'My reply is no', 'My sources say no',
'Outlook not so good', 'Very doubtful']

defaults = default_positive + default_neutral + default_negative
#user_input = input('Ask any question you would like to ask the Magic 8 Ball: ')
random_answer = random.randint(0,19)
print(defaults[random_answer])
