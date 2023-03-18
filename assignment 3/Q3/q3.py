import os

def count_words(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
        return {word.strip('\'",.():;-_') for word in words}

def score_document(query, filename):
    query_words = query.split()
    document_words = count_words(filename)
    score = 0
    for word in query_words:
        if word in document_words:
            score += 1
    return score

def find_highest_score(query, n):
    max_score = -1
    max_filename = ''
    for i in range(1, n+1):
        filename = os.path.join(os.path.dirname(__file__), str(i) + '.txt')
        if os.path.isfile(filename):
            score = score_document(query, filename)
            if score > max_score:
                max_score = score
                max_filename = filename
            elif score == max_score and filename < max_filename:
                max_filename = filename
    return int(os.path.splitext(os.path.basename(max_filename))[0])

n = int(input())
query = input().strip()
print(find_highest_score(query, n))
