from didtoday.file import File
from datetime import date


def add(args):
    if content := args.content:
        today = File(date.today())
        if not today.exists():
            today.create()
        today.add_entry(content)


def show(args):
    if date_to_show := args.date:
        d = compile_date(date_to_show)
        print(File(d).show())
