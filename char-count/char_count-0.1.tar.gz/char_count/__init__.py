def file_count(file):
    try:
        f = open(file, 'r')
        a = len(f.read())
        f.close()
    except IOError:
        return False
    else:
        return a