

def score_libs(data, books):
    score = 0
    book_set = set()
    for library in data['libraries']:
        book_set.update([books[i] for i in library['books_sent']])
    for b in book_set:
        score += b.value
    return score
