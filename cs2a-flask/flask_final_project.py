import random
import string
from isquestion import isQuestion
from isynquestion import isYesNoQuestion
import indicoio
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


""" Takes in a text string and returns a random response from a magic 8-ball. """
def random_response(submission):
    random_answer = random.randint(0, 10 + 9)

    return defaults[random_answer];

""" Main method. This function sets up the main page by returning an HTML template. """
@app.route('/', methods = ['GET','POST'])
def main():

    if request.method == 'POST':
        user_input = request.form['submission']
        submission = user_input.split(' ')

        if isQuestion(submission):

            if isYesNoQuestion(submission):
                response = random_response(submission);
                return render_template("main.html", eightballresponse = response);

            else:
                return render_template("main.html", eightballresponse = "That's not a yes or no question, so I'm not sure. But I think you should.");
        else:
            return render_template("main.html", eightballresponse = "That's not a question. I think.");

""" This function returns the HTML template for the group members involved in this project."""
@app.route('/group')
def group():
    return render_template('group.html')


if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
