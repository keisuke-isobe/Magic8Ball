"""
Function which returns if the input text is a question or not. This is
determined by checking first if the sentence ends with a question mark.
If it does, it is assumed that the statement is a question. If it doesn't
end with a question mark, the function then checks if the statement
contains any of the words that are associated with a question, if it
does, it is considered a question. 
"""
import string
def isQuestion(text, question_words):
    text = text.translate(string.punctuation)
    text = text.lower()
    if text[-1] == '?':
        return True
    else:
        return not set(text).isdisjoint(question_words)
