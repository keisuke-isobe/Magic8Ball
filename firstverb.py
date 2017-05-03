"""
This function returns the highest scoring verb in wordForm. 
"""
def firstVerb(wordForm):
    for token in wordForm:
        if wordForm[token] == "VERB":
            return token
