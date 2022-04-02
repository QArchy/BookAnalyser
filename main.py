import os


def custom_split(sepr_list, str_to_split):
    import re
    regular_exp = '|'.join(map(re.escape, sepr_list))
    return re.split(regular_exp, str_to_split)


class BookAnalyser:
    def __init__(self):
        self.list = list()
        self.separators = list(["\ufeff", "…", "0", "9", "8", "7", "6", "5", "4", "3", "2", "1", "\'", "&", "#", ";",
                                "*", ",", ":", "«", "»", "!", "?", "—", "."])

    def read_book(self, path):
        import sys
        try:
            file = open(path, 'r')  # or os.remove(path)
        except FileNotFoundError:
            print(f"File {path} not found!", file=sys.stderr)
            return
        except PermissionError:
            print(f"Insufficient permission to read {path}!", file=sys.stderr)
            return
        except IsADirectoryError:
            print(f"{path} is a directory!", file=sys.stderr)
            return
        self.list = list((map(lambda x: x.lower(), ' '.join(custom_split(self.separators, file.read())).split())))

    def get_most_words(self, min_word_len=1, words_quantity=1, most_frequent_words=True):
        try:
            self.list[0]
        except IndexError:
            return None
        lst = [y for y in self.list if len(y) >= min_word_len]
        dictionary = dict.fromkeys(lst, 0)
        list(map(lambda x: dictionary.update({x: dictionary.get(x) + 1}), lst))
        return sorted(dictionary.items(), key=lambda x: x[1], reverse=most_frequent_words)[0:words_quantity]


BA = BookAnalyser()
BA.read_book(os.path.abspath(os.getcwd()) + "/War_and_peace.txt")
print(BA.get_most_words(4, 20, True))
