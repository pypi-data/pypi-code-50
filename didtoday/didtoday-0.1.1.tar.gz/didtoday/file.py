import os
from datetime import date
from didtoday.constants import ROOT


class File:
    def __init__(self, d: date) -> None:
        self.date = d

    def strdate(self) -> str:
        return self.date.strftime("%Y-%m-%d")

    def title(self) -> str:
        return f"# {self.strdate()}"

    def path(self) -> str:
        return self.date.strftime(f"{ROOT}/%Y/%m/%d.md")

    def create(self) -> None:
        os.makedirs(os.path.dirname(self.path()), exist_ok=True)

        with open(self.path(), "w+") as f:
            f.write(f"{self.title()}\n\n")

    def add_entry(self, content: str) -> None:
        with open(self.path(), "a+") as f:
            f.write(f"* {content}\n")

    def exists(self) -> bool:
        return os.path.exists(self.path())

    def show(self) -> str:
        with open(self.path()) as f:
            return f.read()
        return ""
