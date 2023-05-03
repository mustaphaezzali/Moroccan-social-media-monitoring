import re
import datetime

import math
import pandas as pd
from collections import defaultdict
from pyarabic import araby
import pickle
# Define the Arabic and English date format strings
arabic_format = '%A %d %B %Y - %H:%M'
english_format = '%A, %B %d, %Y - %I:%M %p'

# Define the regular expression pattern for the Arabic date
pattern = r'^(\S+)\s+(\d+)\s+(\S+)\s+(\d+)\s*-\s*(\d+):(\d+)$'

# Extract the individual date components using the regular expression
match = re.match(pattern, 'الإثنين 24 أبريل 2023 - 16:00')

# Convert the month name to a number
months = {'يناير': 1, 'فبراير': 2, 'مارس': 3, 'أبريل': 4, 'مايو': 5, 'يونيو': 6, 'يوليو': 7, 'أغسطس': 8, 'سبتمبر': 9, 'أكتوبر': 10, 'نوفمبر': 11, 'ديسمبر': 12}

# Create a datetime object from the date components


def transform(arabic_date):
    match = re.match(pattern, arabic_date)
    day_name, day, month_name, year, hour, minute = match.groups()
    month = months[month_name]
    date_object = datetime.date(int(year), month, int(day))
    return date_object,int(day)

def transform_for_comment(arabic_date):
    match = re.match(pattern, arabic_date)
    day_name, day, month_name, year, hour, minute = match.groups()
    month = months[month_name]
    date_object = datetime.date(int(year), month, int(day))
    return date_object.strftime('%Y-%m-%d')



class ArabicTfidfVectorizer:
    def __init__(self):
        self.term_document_frequency = defaultdict(set)
        self.documents = pd.DataFrame(columns=["docno", "content"])

    def _calculate_query_tfidf(self, docs, term_document_frequency):
        tfidf_matrix = []

        for doc in docs:
            tfidf_vector = {}
            tokens = araby.tokenize(doc)
            token_count = len(tokens)
            term_counts = defaultdict(int)

            for term in tokens:
                term_counts[term] += 1

            for term, count in term_counts.items():
                if term in term_document_frequency:
                    tf = count / token_count
                    idf = math.log(len(self.documents) / len(term_document_frequency[term]))
                    tfidf = tf * idf
                    tfidf_vector[term] = tfidf

            tfidf_matrix.append(tfidf_vector)

        return tfidf_matrix

    def transform(self, docs):
        return self._calculate_query_tfidf(docs, self.term_document_frequency)
    
    def fit_transform(self, docs):
        self.documents = docs
        self.term_document_frequency = self._calculate_term_document_frequency()
        return self._calculate_tfidf(self.documents, self.term_document_frequency)

    def _calculate_term_document_frequency(self, docs=None):
        if docs is None:
            docs = self.documents
        term_document_frequency = defaultdict(set)
        for doc_id, doc in docs.iterrows():
            tokens = araby.tokenize(doc['content'])
            unique_terms = set(tokens)
            for term in unique_terms:
                term_document_frequency[term].add(doc_id)
        return term_document_frequency

    def _calculate_tfidf(self, docs, term_document_frequency):
        tfidf_matrix = []

        for doc_id, doc in docs.iterrows():
            tfidf_vector = {}
            tokens = araby.tokenize(doc['content'])
            token_count = len(tokens)
            term_counts = defaultdict(int)

            for term in tokens:
                term_counts[term] += 1

            for term, count in term_counts.items():
                tf = count / token_count
                idf = math.log(len(docs) / len(term_document_frequency[term]))
                tfidf = tf * idf
                tfidf_vector[term] = tfidf

            tfidf_matrix.append(tfidf_vector)

        return tfidf_matrix
    
