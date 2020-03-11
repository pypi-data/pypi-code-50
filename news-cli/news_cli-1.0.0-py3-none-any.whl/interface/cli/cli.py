"""
Cli interface

"""
import webbrowser
import click
from prettytable import PrettyTable
from news.src.google_news import get_headlines, get_keyword_news


@click.group(invoke_without_command=True, help="Read news on your command line.")
@click.pass_context
@click.option('--area', default='USA', show_default=True, help="Area of interest")
@click.option('--keyword', default=None, show_default=True, help="Specific news for the keyword")
def main(ctx, area, keyword):
    """
    Default

    :return:
    """

    ctx.obj = {}

    if keyword is None:
        result = get_headlines(area)
    else:
        result = get_keyword_news(keyword)

    table = PrettyTable()

    table.field_names = ["#", "Title"]
    for i, res in enumerate(result):
        table.add_row([i + 1, res[0]])
        ctx.obj[i+1] = res[2]

    table.align["Title"] = "l"
    print(table)

    if len(result) > 0:
        value = click.prompt('Open url# in a browser (Press Enter to exit)', type=int, default=0)
        while 0 < value < len(result):
            webbrowser.open(ctx.obj[value])
            value = click.prompt('Open url# in a browser (Press Enter to exit)', type=int, default=0)

    print("Ciao! Come back for news bulletin.")


if __name__ == "__main__":
    main({})
