from coderadio.tui import app
from coderadio.core import initialize_services


def main():
    initialize_services()
    app.run()
