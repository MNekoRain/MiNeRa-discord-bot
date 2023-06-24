
def question(text):
    input(f'\033[47m\033[30m[QUESTION]\033[0m{text}')


def warn(text):
    print(f'\033[43m\033[30m[WARN]\033[0m{text}')


def error(text):
    print(f'\033[41m\033[30m[ERROR]\033[0m{text}')


def info(text):
    print(f'\033[47m\033[30m[INFO]\033[0m{text}')
