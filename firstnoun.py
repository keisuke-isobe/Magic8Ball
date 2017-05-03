"""
This function returns the highest scoring noun in wotdForm.
"""
def firstNoun(wordForm):
    for token in wordForm:
        if wordForm[token] == "NOUN":
            return token
