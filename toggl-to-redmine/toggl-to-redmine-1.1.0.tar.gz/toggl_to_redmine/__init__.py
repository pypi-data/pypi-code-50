from toggl_to_redmine.CLI import CLI
import click


@click.command()
def main():
    CLI().entry_point()


main()
