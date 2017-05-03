"""
This function returns the keywords found in the user input statement. This
function removes keywords that are longer than one word, because we only want
a dictionary that contains singe-word entries.
"""
def keywords(user_input):
    keywords = indicoio.keywords(user_input, top_n = 5)
    for k in list(keywords.keys()):
        s = k.split(" ")
        if len(s) > 1:
            del(keywords[k])
    return keywords
