import json
from typegame.core.question_class import Question


def handle_error(e, line, explanation):
    explanation.append("error in line: {}".format(line.strip()))
    explanation.append("{} -> {}".format(type(e).__name__, e))


def parse_snippet(snippet: list, type_only=True):
    explanation = []
    if snippet:
        line = snippet[-1]
    else:
        line = "None"
    has_error = False

    try:
        exec("".join(snippet), locals())
    except Exception as e:
        handle_error(
            e, snippet[e.__traceback__.tb_next.tb_lineno - 1], explanation
        )
        has_error = True

    try:
        if type_only:
            answer = eval(f"type({line.strip()}).__name__", locals())
        else:
            answer = str(eval(line.strip(), locals()))
        answer_value = str(eval(line.strip(), locals()))
    except Exception as e:
        answer = "error"
        answer_value = "error"
        handle_error(e, line, explanation)

    if has_error:
        answer = "error"

    explanation.append("%s --> %s" % (line, answer_value))

    return Question(
        answer=answer,
        answer_value=answer_value,
        _code_lines=snippet,
        _explanation_lines=explanation,
    )


def parse_notebook(nb_loc, type_only=True):

    questions = []
    for cell in json.load(open(nb_loc, "r"))["cells"]:
        if (cell["cell_type"] == "code") and (len(cell["source"]) > 0):
            questions.append(parse_snippet(cell["source"], type_only))

    all_answers = [q.answer for q in questions]
    for q in questions:
        q.alternates = set(all_answers.copy())
    return questions
