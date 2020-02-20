import argparse

from backtrack import solve
from dataHandler import reader, parser, libs_to_writer, writer
from greedy import get_greedy

if __name__ == "__main__":

    argparser = argparse.ArgumentParser()
    argparser.add_argument('--f', help="letter_to_load", type=str, default='a')
    args = argparser.parse_args()

    filename = {
        'a': 'data/a_example.txt',
        'b': 'data/b_read_on.txt',
        'c': 'data/c_incunabula.txt',
        'd': 'data/d_tough_choices.txt',
        'e': 'data/e_so_many_books.txt',
        'f': 'data/f_libraries_of_the_world.txt'
    }[args.f]

    b, l, days = parser(reader(filename))

    libs, s = solve(b, l, days, verbose=False)

    ans = libs_to_writer(libs, days)
    print("ans", ans)
    writer(ans, "test.txt")
