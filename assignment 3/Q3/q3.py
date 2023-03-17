import os
import sys

# define a function to calculate the score of a document with respect to a query
def calculate_score(query, document):
    # split the query and document into words
    query_words = query.split()
    with open(document, 'r') as file:
        document_words = file.read().split()

    # calculate the score as the number of common words between query and document
    score = len(set(query_words) & set(document_words))
    return score

# get the total number of documents
n = int(input())

# create a list of document names
documents = [f"{i}.txt" for i in range(1, n+1)]

# get the query from the user
query = input()

# calculate the score for each document and store the max score and corresponding document
max_score = -1
max_document = ''
for document in documents:
    score = calculate_score(query, document)
    if score > max_score:
        max_score = score
        max_document = document
    elif score == max_score:
        max_document = min(max_document, document)

# print the name of the document with the maximum score
print(os.path.splitext(max_document)[0])