# -*- coding: utf-8 -*-
'''
# Text Preprocessing Pipeline
#
# Credit: Dipanjan Sarkar for core text preprocessing pipeline,
#         I've simply refactored the code a bit, and re-wrote his
#         pipeline to learn how everything works myself.
#
# Pipeline
# 
# 1. Strip HTML from text
# 2. Remove accented characters
# 3. Expand contractions
# 4. Remove special characters
# 5. Stemming and lemmatization
# 6. Remove Stopwords
#
# Reference: Practical Machine Learning with Python by Dipanjan Sarkar
'''

import re
import nltk
import spacy
import unicodedata
from bs4 import BeautifulSoup 
from contractions import contraction_dict
from nltk.tokenize.toktok import ToktokTokenizer

# Strip HTML
def strip_html(text):
    # Instantiate BSoup object html.parser
    s = BeautifulSoup(text, "html.parser")
    cleaned_text = s.get_text()
    return cleaned_text

# Remove accented characters
def remove_accents(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

# Expand Contractions
def expand_contractions(text, contractions=contraction_dict):
    # Create reg-exp pattern
    contraction_pattern = re.compile('({})'.format('|'.join(contractions.keys())), 
                                      flags=re.IGNORECASE|re.DOTALL)
    # Expanding Contactions
    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contractions.get(match) \
                                   if contractions.get(match) \
                                    else contractions.get(match.lower())                       
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction
    
    # Create your output
    expanded_text = contraction_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text

# Remove Special Characters
def remove_special_characters(text):
    # Use regex to sub
    text = re.sub('[^a-zA-Z0-9\s]', '', text)
    return text

# Removing Stopwords
nlp = spacy.load('en', parse = False, tag=False, entity=False)
tokenizer = ToktokTokenizer()
stopword_list = nltk.corpus.stopwords.words('english')
stopword_list.remove('no')
stopword_list.remove('not')

def remove_stopwords(text, lower_case=False):
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]

    # Check if lowercase for filter
    if lower_case:
        filtered_tokens = [token for token in tokens if token not in stopword_list]
    else:
        filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]

    filtered_tokens = ' '.join(filtered_tokens)
    return filtered_tokens

# Lemmatize Text
def lemmatize_text(text):
    text = nlp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    return text

# Remove extract newlines
def remove_new_lines(text):
    text = re.sub(r'[\r|\n|\r\n]+', ' ', text)
    return text

# Insert spaces for special characters
def insert_special_chars(text):
    spec_pattern = re.compile(r'([{.(-)!}])')
    text = spec_pattern.sub(" \\1 ", text)
    return text

#
# MAIN CORPUS CLEARNING PIPELINE, corpus is array of documents
#
def normalize_text(corpus, html_stripping=True, contraction_expansion=True,
                   accented_char_remove=True, text_lower_case=True,
                   text_lemmatization=True, special_char_removal=True,
                   stopword_removal=True):

    normalized_corpus = []
    
    #
    # Normalizes each document in a corpus
    #
    for document in corpus:
        # 1. Strip HTML from text
        if html_stripping:
            document = strip_html(document)
        
        # 2. Remove accented characters
        if accented_char_remove:
            document = remove_accents(document)
        
        # 3. Expand contractions
        if contraction_expansion:
            document = expand_contractions(document)

        # 4. Make document all lowercase
        if text_lower_case:
            document = document.lower()
        
        # 5. Remove Newlines from text using regex
        document = remove_new_lines(document)

        # 6. Insert spaces between special characters to isolate
        document = insert_special_chars(document)

        # 7. Lemmatization
        if text_lemmatization:
            document = lemmatize_text(document)
        
        # 8. Remove Special characters
        if special_char_removal:
            document = remove_special_characters(document)
        
        # 9. Remove Extra whitespace
        document = re.sub(' +', ' ', document)
        
        # 10. Remove Stopwords
        if stopword_removal:
            document = remove_stopwords(document, lower_case=text_lower_case)
        
        # 11. Add normalized document to corpus
        normalized_corpus.append(document)
    
    return normalized_corpus

#
# MAIN
#
def main():
    # testing out functions here..
    return 0

if __name__ == '__main__':
    main()



