"""
This flask app presents a webpage which acts as an interactive Magic 8 Ball. It has a
larger variety of responses (and more ambiguity) than your traditional Magic 8 Ball.
There are two necessary APIs for this project: the indico.io API which was used in class,
and the Google Cloud Natural Language Processing API: https://cloud.google.com/natural-language/

Something interesting: We used the indic.io and Google Cloud Natural Language Processing API
to determine the highest importance noun in the user input question if the user input question
was not a simple yes/no question, and used that extracted noun in the Magic 8 Ball's
vague, non-committal response to make it seem a bit more intelligent.
"""
import random
import string
import indicoio
import operator
indicoio.config.api_key = 'f954e20684d172b9ebcc869bc9fac4b1'
from google.cloud import language
language_client = language.Client()

from flask import Flask, render_template, request
app = Flask(__name__)

default_positive = ['It is certain', 'It is decidedly so', 'Without a doubt',
'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
'Yes', 'Signs point to yes']
default_neutral = ['Reply hazy, try again', 'Ask again later', 'Better not to tell you now',
'Cannot predict now', 'Concentrate and ask again']
default_negative = ['Don\'t count on it', 'My reply is no', 'My sources say no',
'Outlook not so good', 'Very doubtful']

defaults = default_positive + default_neutral + default_negative

wh_words = ["who", "what", "when", "where", "which", "who", "whom", "whose", "why", "how"]
yn_words = ["can", "could", "may", "might", "shall", "should", "will", "would", "must", "ought", "be", "do", "have"]

question_words = wh_words + yn_words


"""
Function which returns if the input text is a question or not. This is
determined by checking first if the sentence ends with a question mark.
If it does, it is assumed that the statement is a question. If it doesn't
end with a question mark, the function then checks if the statement
contains any of the words that are associated with a question, if it
does, it is considered a question.
"""

def isQuestion(text):
    text = text.translate(string.punctuation)
    text = text.lower()
    if text[-1] == '?':
        return True
    else:
        return not set(text).isdisjoint(question_words)


"""
Function which returns whether or not a passed statement is a yes-no question or
not. Yes-no questions are asked with the verbs "be," "do," "have," or a modal/
auxiliary verb. The function here checks whether or not the statement contains
any of these verbs, and if so, returns true. Otherwise it returns false.
"""

def isYesNoQuestion(text):
    text = text.translate(string.punctuation)
    text = text.lower()
    text = text.split(" ")

    return not set(text).isdisjoint(yn_words)


"""
Takes in a text string and returns a random response from a magic 8-ball.
"""
def random_response(submission):
    random_answer = random.randint(0, 10) + random.randint(0,9)
    return defaults[random_answer];

"""
This function returns the keywords found in the user input statement. This
function removes keywords that are longer than one word, because we only want
a dictionary that contains singe-word entries.
"""
def keyword(user_input):
    keywords = indicoio.keywords(user_input, top_n = 5)
    for k in list(keywords.keys()):
        s = k.split(" ")
        if len(s) > 1:
            del(keywords[k])
    return keywords

"""
This function takes the keywords dictionary returned by the indicoio keywords
function and returns it in sorted order from highest to lowest importance, in
string format.
"""
def sortKeywords(keywords):
    sorted_keywords = sorted(keywords.items(), key = operator.itemgetter(1), reverse = True)
    sorted_keywords_keys = []
    for i in range(0,len(sorted_keywords)):
        sorted_keywords_keys.append(sorted_keywords[i][0])
    sorted_keywords_keys = " ".join(str(s) for s in sorted_keywords_keys)
    return sorted_keywords_keys

"""
Function that returns a dictionary that contains a keyword and it's part
of speech.
"""
def wordForm(sorted_keywords):
    document = language_client.document_from_text(sorted_keywords)
    annotations = document.annotate_text().tokens
    words = {}
    for token in annotations:
        word = token.text_content
        pos = token.part_of_speech
        words[word] = pos
    return words

"""
This function returns the highest scoring noun in wotdForm.
"""
def firstNoun(wordForm):
    for token in wordForm:
        if wordForm[token] == "NOUN":
            return token
    return -1
"""
Main method. This function sets up the main page by returning an HTML template.
"""
@app.route('/', methods = ['GET','POST'])
def main():

    if request.method == 'POST':
        user_input = request.form['submission']
        submission = user_input.split(' ')
        submission = request.form['submission']
        if isQuestion(submission):
            if isYesNoQuestion(submission):
                response = random_response(submission);
                return render_template("main.html", eightballresponse = response);
            else:
                keywords = keyword(submission)
                sorted_keywords = sortKeywords(keywords)
                words = wordForm(sorted_keywords)
                noun = firstNoun(words)
                response = "That's not a yes or no question, so I'm not sure about this answer..."
                if noun != -1:
                    if (noun == "lunch" or noun == "breakfast" or noun == "dinner"):
                        response = reponse + "I don't know what you should about " + noun + "."
                    else:
                        response = response + "I don't know what you should do about the " + noun + "."
                return render_template("main.html", eightballresponse = response);
        else:
            return render_template("main.html", eightballresponse = "That's not a question. I think.");

    else:
        return render_template("main.html", eightballresponse = "You didn't ask me anything.");

""" This function returns the HTML template for the group members involved in this project."""
@app.route('/group')
def group():
    return render_template('group.html')


if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
