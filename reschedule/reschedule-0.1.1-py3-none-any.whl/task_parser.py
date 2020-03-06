import re
import typing as t
from datetime import datetime

from .models import ParserContext, Task, TaskStatus

from .config import default_est


def _get_status_from_char(char: str) -> TaskStatus:
    """Convert the character in the [ ] for a task into a TaskStatus

    Args:
        char (str): the character in the brackets of a task

    Raises:
        Exception: If the character is not mapped to a TaskStatus

    Returns:
        TaskStatus: The status of the task.
    """
    if char == "c":
        return TaskStatus.CANCELED
    elif char == "b":
        return TaskStatus.BLOCKED
    elif char == " ":
        return TaskStatus.UNSCHEDULED
    elif char == "x":
        return TaskStatus.DONE
    elif char == "?":
        return TaskStatus.IDEA
    elif char == "-":
        return TaskStatus.IN_PROGRESS
    else:
        raise Exception("unknown status character {char}".format(char=char))


# the parser
class TaskParser(object):
    def __init__(self):
        super().__init__()
        self.parser_context: ParserContext = ParserContext.NONE
        self.date_context: datetime.date
        self.tasks: t.List[Task] = []
        self.task_ids = set()
        self.indent_type = None
        self.indent_level_to_task: t.Dict[Task] = dict()

    def _parse_line(self, line: str, line_number: int):
        # ignore white space lines
        if re.fullmatch(r"\s+", line):
            pass
        # context lines start with '//'
        elif line.startswith("//"):
            try:
                new_date_context = datetime.strptime(
                    line[2:].strip(), "%Y-%m-%d"
                ).date()
                self.date_context = new_date_context
                self.parser_context = ParserContext.TASK
            # TODO(lukemurray): fail if unknown context
            except ValueError:
                self.parser_context = ParserContext.NONE
        else:
            # parse non blank and non context lines based on the current context
            if self.parser_context == ParserContext.TASK:
                self._parse_task(line, line_number)
            elif self.parser_context == ParserContext.NONE:
                pass
            else:
                raise Exception(
                    "no parsing handled for parse context {context}".format(context=self.parser_context)
                )

    def _check_indent(self, indent: str, line_number: str):
        if len(indent) != 0:
            all_tabs = all(c == "\t" for c in indent)
            all_spaces = all(c == " " for c in indent)
            if all_tabs or all_spaces:
                expected_indent_type = "tabs" if all_tabs else "spaces"
                if self.indent_type is None:
                    self.indent_type = expected_indent_type
                elif self.indent_type != expected_indent_type:
                    raise Exception(
                        "Prev indent character {indent_type} does not \
                            match indent character {expected_indent_type} on \
                                line {line_number}".format(indent_type=self.indent_type, expected_indent_type=expected_indent_type, line_number=line_number)
                    )
            else:
                raise Exception(
                    "Please do not mix tabs and spaces in your task indent (line: {line_number})".format(line_number=line_number)
                )

    def _parse_task(self, line: str, line_number: int):
        new_task = Task()
        # make sure the line starts with spaces followed by - [ ] there can be any character in the brackets
        task_status_regex = r"(\s*)\- \[(.?)\]"
        task_status_match = re.match(task_status_regex, line)
        if not task_status_match:
            raise Exception("(line {line_number}) todos must start with - [ ]".format(line_number=line_number))
        else:
            assert task_status_match is not None
            indent: str = task_status_match.group(1)
            self._check_indent(indent, line_number)
            status_char = task_status_match.group(2)
            new_task.status = _get_status_from_char(status_char)

        # add people to task
        person_regex = r"@(\w+)"
        people = re.finditer(person_regex, line)
        for person_match in people:
            new_task.people.append(person_match.group(1))

        # add project to task
        project_regex = r"\+(\w+)"
        projects = re.finditer(project_regex, line)
        for project_match in projects:
            new_task.projects.append(project_match.group(1))

        # get the tags as a dict
        tag_regex = r"(\w+):([\w|\-]+)"
        tags = re.finditer(tag_regex, line)
        tag_dict: t.Dict[str, str] = dict()
        for tag_match in tags:
            tag_dict[tag_match.group(1)] = tag_match.group(2)
        if "id" not in tag_dict:
            raise Exception("(line {line_number}) task is missing an id".format(line_number=line_number))
        # add the id to the task
        new_task.id = tag_dict["id"]
        if new_task.id in self.task_ids:
            raise Exception("duplicate ids")
        self.task_ids.add(new_task.id)

        # TODO(lukemurray): maybe depreacted by the date tag
        # add the date to the task
        new_task.date = self.date_context

        # parse the estimate tag
        est = tag_dict.get("est", default_est)
        est_regex = r"(\d+)(\w+)"
        est_in_minutes = 30
        est_match = re.fullmatch(est_regex, est)
        if est_match is not None:
            measure = est_match.group(1)
            unit = est_match.group(2)
            if unit == "m":
                est_in_minutes = int(measure)
            elif unit == "h":
                est_in_minutes = 60 * int(measure)
            else:
                raise Exception("unknown unit {unit}".format(unit=unit))

        # add the estimate to the task
        new_task.estimate = est_in_minutes

        # description from removing status and tags
        new_task.description = (
            re.sub(tag_regex, "", re.sub(task_status_regex, "", line))
            .replace("\n", "")
            .replace("\t", "")
            .strip()
        )

        new_task.line_number = line_number

        # manage indent dependencies
        # indent level is like the number of spaces and can be 1, 2, 3, 4 etc.
        # semantic indent level is just based on hiearchy and ignored cardinality
        # indirection to ignore spacing issues and provide nice indexing
        indent_level = len(indent)
        self.indent_level_to_task[indent_level] = new_task
        all_indent_levels = sorted(list(self.indent_level_to_task.keys()))
        semantic_indent_level = all_indent_levels.index(indent_level)
        if semantic_indent_level != 0:
            parent_task = self.indent_level_to_task[
                all_indent_levels[semantic_indent_level - 1]
            ]
            parent_task.children.append(new_task)

        # due date
        if "due" in tag_dict:
            due_date = datetime.strptime(tag_dict["due"], "%Y-%m-%d").date()
            new_task.due_date = due_date

        self.tasks.append(new_task)

    def parse(self, file: str):
        with open(file, "r") as f:
            for line_number, line in enumerate(f):
                self._parse_line(line, line_number)

    def get_tasks(self, file: str):
        self.parse(file)
        return self.tasks
