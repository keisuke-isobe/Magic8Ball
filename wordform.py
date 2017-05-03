"""
Function that returns a dictionary that contains a keyword and it's part
of speech.
"""
def wordForm(sorted_keywords):
    document = language_client.document_from_text(sorted_keywords)
    annotations = document.annotate_text().tokens
    wordForm = {}
    for token in annotations:
        word = token.text_content
        pos = token.part_of_speech
        wordForm[word] = pos
    return wordForm
