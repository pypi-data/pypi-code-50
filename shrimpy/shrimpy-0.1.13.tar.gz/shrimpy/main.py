from fire import Fire
from shrimpy import check, contextualize, load, quit, run


def play(directory = "", start_key = "start"):
    directory = contextualize(directory)
    valid, json_file_paths, response = check(directory)
    if not valid:
        return valid, response
    game = load(json_file_paths)
    run(start_key, game)
    quit()


def validate(directory = ""):
    directory = contextualize(directory)
    valid, json_file_paths, response = check(directory)
    return valid, response


def activate():
    Fire({
        'play': play,
        'validate': validate
    })


if __name__ == '__main__':
    run()
