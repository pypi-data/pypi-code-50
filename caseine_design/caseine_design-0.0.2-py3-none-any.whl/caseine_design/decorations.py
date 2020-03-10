"""A set of semantic-less decorations that are used to pinpoint functions
that the VPL design plugin will modify to generate student requested files
or genarate test comparator files."""


def todoin(_func=None, *, comment=None):
    """States that a function body should be removed from the student requested
    file, while keeping its declaration and profile + documentation."""

    def decorator_todoin(func):
      return func

    if _func is None:
      return decorator_todoin
    else:
      return decorator_todoin(_func)



def todo(_func=None, *, comment=None):
    """States that a function should be entirely removed from the student
    requested file. If keyword comment is provided, then a comment with the
    specified content will be added in place of the function."""

    def decorator_todo(func):
        return func

    if _func is None:
        return decorator_todo
    else:
        return decorator_todo(_func)
