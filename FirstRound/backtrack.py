import operator

def super_greed(book, libraries, days):
    libraries = sorted(libraries, key=operator.attrgetter('sign_time'))
    r = []
    for lib in libraries:
        days -= lib.sign_time
        if days >= 0:
            r.append(lib)
    return r

def solve(books, libraries, days, verbose=False):
    # score libraries
    for l in libraries:
        l.score(days)
        l.set_max_value()
    # sort ascendingly
    libraries = sorted(libraries, key=operator.attrgetter('max_score'), reverse=True)
    current_score = 0
    added_libraries = []
    lib_removed = {}
    void_books = set()
    for i, lib in enumerate(libraries):
        days -= lib.sign_time
        current_score += lib.score(days, void_books)
        added_libraries.append(lib)
        lib_removed[lib] = set(lib.books)
        void_books = void_books.union(set([b.id for b in lib.books]))
        if verbose:
            print(f"Adding lib of value {lib.max_score} - days lefts {days+lib.sign_time} -> {days}")
        if days <= 0:
            d = abs(days)
            for j, n_lib in enumerate(added_libraries[::-1]):
                if n_lib.sign_time > d:
                    j = len(added_libraries)-j-1
                    break
            L = added_libraries[j] 
            if verbose:
                print(f"Too big, removing lib of score {L.max_score} taking {L.sign_time}")
            added_libraries.remove(L)
            [void_books.remove(book.id) for book in lib_removed[L] if book.id in void_books]
            current_score -= L.score(days)
            days += L.sign_time
    return added_libraries, current_score