import json
import glob
import os
import datetime

import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State

from typegame.parsing.from_notebook import parse_notebook
from typegame.parsing.to_components import (
    parse_leaderboard,
    parse_question_list,
    get_question_solution_layout,
)
from typegame.core.submission_class import Submission


from typing import List, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from typegame.core.question_class import Question  # noqa: F401


def decorate_app(
    app: dash.Dash, quiz_path: str, answer_path: str, type_only: bool = True
) -> None:
    @app.callback(
        Output("leaderboard", "children"),
        [Input("interval-component", "n_intervals")],
    )
    def update_leaderboard(_):
        js_files = glob.glob(os.path.join(answer_path, "*.json"))
        board_components = parse_leaderboard(
            [Submission(**json.load(open(jf))) for jf in js_files]
        )
        return board_components

    @app.callback(
        Output("question_list", "children"), [Input("quiz_list", "value")]
    )
    def get_question_list_for_quiz(quiz_name):
        if quiz_name is not None:
            return parse_question_list(
                parse_notebook(
                    os.path.join(quiz_path, f"{quiz_name}.ipynb"), type_only
                )
            )

    @app.callback(
        [
            Output("output-state", "children"),
            Output("warning-msg", "children"),
            Output("question_list", "style"),
            Output("form-submit", "style"),
        ],
        [Input("submit-button", "n_clicks"), Input("quiz_list", "value")],
        [State("name", "value"), State("question_list", "children")],
    )
    def evaluate_submission(n_clicks, quiz_name, name, answers):
        if (n_clicks < 1) or (answers is None):
            return [], [], {}, {}
        question_list = parse_notebook(
            os.path.join(quiz_path, f"{quiz_name}.ipynb"), type_only
        )
        parsed_answers = [
            a["props"]["children"][2]["props"].get("value") for a in answers
        ]

        return handle_submission(
            question_list, parsed_answers, quiz_name, name, answer_path
        )


def handle_submission(
    question_list: List["Question"],
    answers: list,
    quiz_name: str,
    name: str,
    answer_path: str,
) -> Tuple:

    correct_num = 0
    solutions = []
    missed = []

    for idx, question in enumerate(question_list):
        user_answer = answers[idx]
        if user_answer is None:
            missed.append(idx + 1)
        else:
            is_correct = question.answer == user_answer
            correct_num += int(is_correct)
            solutions.append(
                get_question_solution_layout(
                    question, user_answer, idx, is_correct
                )
            )
    if len(missed) > 0:
        return (
            [],
            "You did not answer questions {}".format(
                ", ".join([str(m) for m in missed])
            ),
            {},
            {},
        )

    json.dump(
        Submission(
            name=name,
            answers=answers,
            correct_answers=correct_num,
            quiz_name=quiz_name,
        ).dict(),
        open(
            os.path.join(
                answer_path, f"{name}-{datetime.datetime.now()}.json"
            ),
            "w",
        ),
    )

    header = html.H2("{}/{}".format(correct_num, len(solutions)))
    return (
        html.Div([header, *solutions]),
        "",
        {"display": "none"},
        {"display": "none"},
    )
