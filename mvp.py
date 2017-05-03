"""
Minimum Viable Product Magic 8 Ball

Very simple, takes user input question, and returns a random answer from the set
of 20 standard Magic 8 Ball responses.

"""

import random

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
