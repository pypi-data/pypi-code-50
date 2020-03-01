from sqlview import DB


def dump(path):
    db = DB(path)
    for table in db.tables:
        for row in table:
            print(row)


def stats(path):
    db = DB(path)
    print(path)
    for table in db.tables:
        print(f'\t{table.name} : {len(table)}')


