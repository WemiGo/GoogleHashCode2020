import operator

def solve(books, libraries, days, verbose=False):
    # score libraries
    for l in libraries:
        l.score(days)
        l.set_max_value()
    # sort ascendingly
    libraries = sorted(libraries, key=operator.attrgetter('max_score'), reverse=True)
    current_score = 0
    added_libraries = []
    for i, lib in enumerate(libraries):
        days -= lib.sign_time
        current_score += lib.score(days)
        added_libraries.append(lib)
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
            current_score -= L.score(days)
            days += L.sign_time
    return added_libraries, current_score