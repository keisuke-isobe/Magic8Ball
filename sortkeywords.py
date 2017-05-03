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
