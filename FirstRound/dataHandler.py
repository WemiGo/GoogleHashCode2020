from classes import Library, Book

def parser(data):

    books = []
    for _id, value in zip(range(data['total_books']), data['book_scores']):
        books.append(Book(_id, value))

    libraries = []
    for _id, lib in enumerate(data['libs']):
        libraries.append(Library(
            _id,
            [books[i] for i in lib['books_held']],
            lib['signup_time'],
            lib['ship_rate'])
        )
    return books, libraries, data["days"]

def libs_to_writer(libs, days):
    data = dict()
    data["signed_libraries"] = len(libs)
    data["libraries"] = [dict() for _ in libs]
    days_left = days
    for i, l in enumerate(libs):
        data["libraries"][i]["id"] = l.id
        days_left -= l.sign_time
        data["libraries"][i]["num_books_sent"] = l.scan_cap * days_left
        l.sort_books()
        data["libraries"][i]["books_sent"] = [b.id for b in l.books]
    return data


def writer(data, filename):
    # Data must be of this EXACT format
    # data = {
    #     'signed_libraries': 2,
    #     'libraries': [
    #         {
    #             'id': 1,
    #             'num_books_sent': 3,
    #             'books_sent': [5, 2, 3]
    #         },
    #         {
    #             'id': 0,
    #             'num_books_sent': 5,
    #             'books_sent': [0, 1, 2, 3, 4]
    #         }
    #     ]
    # }
    with open(filename, 'w') as f:
        f.write(str(data['signed_libraries']) + "\n")
        for library in data['libraries']:
            f.write(f"{library['id']} {library['num_books_sent']}\n")
            f.write(str(library['books_sent'])[1:-1].replace(',', '') + "\n")

def reader(filename):
    f = open(filename, "r")
    res = dict()
    l1 = f.readline().split()
    res["total_books"] = int(l1[0])
    res["num_lib"] = int(l1[1])
    res["days"] = int(l1[2])
    res["book_scores"] = list(map(int,f.readline().split()))
    res["libs"] = [0] * res["num_lib"]
    for i in range(res["num_lib"]):
        res["libs"][i] = dict()
        next_line = list(map(int,f.readline().split()))
        res["libs"][i]["num_books"] = next_line[0]
        res["libs"][i]["signup_time"] = next_line[1]
        res["libs"][i]["ship_rate"] = next_line[2]
        res["libs"][i]["books_held"] = list(map(int, f.readline().split()))
    f.close()
    return res
