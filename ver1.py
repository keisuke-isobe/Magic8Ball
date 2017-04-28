"""
Minimum Viable Product Magic 8 Ball

Very simple, takes user input question, and returns a random answer from the set
of 20 standard Magic 8 Ball responses.

"""

import random
import indicoio
indicoio.config.api_key = 'f954e20684d172b9ebcc869bc9fac4b1'
import semantria
session = semantria.Session('8cf39f38-8d39-4e1c-8f31-52514d897ca2','dea49cf1-88a2-4a69-81eb-0859b0a20a98')

default_positive = ['It is certain', 'It is decidedly so', 'Without a doubt',
'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
'Yes', 'Signs point to yes']

default_neutral = ['Reply hazy, try again', 'Ask again later', 'Better not to tell you now',
'Cannot predict now', 'Concentrate and ask again']

default_negative = ['Don\'t count on it', 'My reply is no', 'My sources say no',
'Outlook not so good', 'Very doubtful']

defaults = default_positive + default_neutral + default_negative

answers = []

user_input = input('Ask any question you would like to ask the Magic 8 Ball: ')
random_answer = random.randint(0,19)
print(defaults[random_answer])
