import random
import string

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

"""
Function which returns if the input text is a question or not. This is
determined by checking first if the sentence ends with a question mark.
If it does, it is assumed that the statement is a question. If it doesn't
end with a question mark, the function then checks if the statement
contains any of the words that are associated with a question, if it
does, it is considered a question. 
"""

def isQuestion(submission):
    text = submission.translate(string.punctuation)
    text = submission.lower()
    
    if text[-1] == '?':
        return True
    else:
        return False;

"""
Function which returns whether or not a passed statement is a yes-no question or
not. Yes-no questions are asked with the verbs "be," "do," "have," or a modal/
auxiliary verb. The function here checks whether or not the statement contains
any of these verbs, and if so, returns true. Otherwise it returns false.
"""

def isYesNoQuestion(submission):
    text = submission.translate(string.punctuation)
    text = submission.lower()

    for word in text:
    	if word in yn_words:
    		return True;
    	else:
    		return False;
    	
    
""" Main method. This function sets up the main page by returning an HTML template. """
@app.route('/', methods = ['GET','POST'])
def main():
        
    if request.method == 'POST':
        submission = request.form['submission']
        
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
