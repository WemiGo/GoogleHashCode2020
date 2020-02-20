import argparse

from dataHandler import reader, parser

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

    b, l = parser(reader(filename))
    print(f"Books \n{b}\nLibraries\n{l}")