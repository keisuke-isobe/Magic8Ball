import indicoio
indicoio.config.api_key = 'f954e20684d172b9ebcc869bc9fac4b1'
# Imports the Google Cloud client library
from google.cloud import language
# Instantiates a client
language_client = language.Client()
# The text to analyze
document = language_client.document_from_text(text)
# Detects the sentiment of the text
annotations = document.annotate_text().tokens
print(type(annotations))
for token in annotations:
    print(token.part_of_speech, token.text_content)
