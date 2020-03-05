from sys import argv

from sqlview import dump, stats


dump_usage = f'''Usage:
    sql_dump {{path}}

    Dumps sqlite file
'''
def sql_dump():
    try:
        path = argv[1]
        open(path, 'rb')
        dump(path)
    except Exception as x:
        print(f'\n ! {x} !\n')
        print(dump_usage)


stats_usage = f'''Usage:
    sql_stats {{path}}

    Stats sqlite file
'''
def sql_stats():
    try:
        path = argv[1]
        open(path, 'rb')
        stats(path)
    except Exception as x:
        print(f'\n ! {x} !\n')
        print(stats_usage)


