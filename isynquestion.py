"""
Function which returns whether or not a passed statement is a yes-no question or
not. Yes-no questions are asked with the verbs "be," "do," "have," or a modal/
auxiliary verb. The function here checks whether or not the statement contains
any of these verbs, and if so, returns true. Otherwise it returns false.
"""
import string
def isYesNoQuestion(text, yn_words):
    text = text.translate(string.punctuation)
    text = text.lower()
    return not set(text).isdisjoint(yn_words)
