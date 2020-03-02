def generate_related_notes(note):
    related_notes_string = f"""
```
### Attachment
[Icon](@attachment/icon.png)
### Note
[Example](@note/Example.md)
### Tag
[Basics](@tag/Basics)
### Search
[linking](@search/linking)
```
"""
    note.add_section("Related Notes", related_notes_string)


def generate_open_questions(note):
    question_string = f"""
1. Question#1
"""
    note.add_section("Open Questions", question_string)


def generate_action_items(note):
    action_string = f"""
- [ ] Action Item
- [ ] Sub action item
"""
    note.add_section("Action Items", action_string)


def generate_table(note):
    table_string = f"""
| Left | Center | Right |
| :--- | :----: | ----: |
| •    | •      | •     |
"""
    note.add_section("Table", table_string)


def generate_math(note):
    math_string = f"""
$$
\\begin{{pmatrix}}
   f(\\alpha) & b \\\\
   a         & f(\\beta)
\\end{{pmatrix}}
$$
"""
    note.add_section("Math", math_string)


def generate_diagram(note):
    diagram_string = f"""
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
"""
    note.add_section("Diagram", diagram_string)
