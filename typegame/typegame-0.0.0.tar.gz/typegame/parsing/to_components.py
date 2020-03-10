import dash_core_components as dcc
import dash_html_components as html


from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from typegame.core.question_class import Question  # noqa: F401
    from typegame.core.submission_class import Submission  # noqa: F401


def parse_question_list(question_list: List["Question"]):
    return [
        html.Div(
            [
                html.H3("snippet {}.".format(i + 1)),
                dcc.Markdown(children=q.md_code),
                dcc.RadioItems(
                    id="q-{}".format(i),
                    options=[
                        {"label": a, "value": a} for a in sorted(q.alternates)
                    ],
                    labelStyle={"display": "inline-block"},
                ),
                html.Hr(),
            ],
            style={
                "textAlign": "left",
                "fontSize": "200%",
                "width": "30%",
                "paddingLeft": "35%",
                "paddingRight": "35%",
            },
        )
        for i, q in enumerate(question_list)
    ]


def get_question_solution_layout(
    question: "Question",
    user_answer: str,
    question_index: int,
    is_correct: bool,
):
    result_description = {True: "CORRECT", False: "WRONG"}
    result_color = {True: "green", False: "red"}
    return html.Div(
        [
            html.H2(
                "Q {}. - {}".format(
                    question_index + 1, result_description[is_correct]
                ),
                style={"backgroundColor": result_color[is_correct]},
            ),
            html.H3("Code:"),
            dcc.Markdown(children=question.md_code),
            html.H3("Explanation:"),
            dcc.Markdown(children=question.explanation),
            html.H3("Answer:"),
            dcc.Markdown(
                [
                    a if a != question.answer else "**{}**".format(a)
                    for a in sorted(question.alternates)
                ]
            ),
            html.H4("You answered {}".format(user_answer)),
            html.A("check it on pythontutor", href=question.pythontutor_link),
            html.Hr(),
        ],
        style={
            "textAlign": "left",
            "fontSize": "200%",
            "width": "30%",
            "padding-left": "35%",
            "padding-right": "35%",
        },
    )


def parse_leaderboard(submission_list: List["Submission"]):

    quiz_boards = {}

    for sub in submission_list:
        quiz_name = sub.quiz_name
        if quiz_name not in quiz_boards.keys():
            quiz_boards[quiz_name] = {}

        user_scores = quiz_boards[quiz_name]

        name = sub.name
        user_dic = {
            "score": "{}/{}".format(sub.correct_answers, len(sub.answers)),
            "correct_answers": sub.correct_answers,
        }
        try:
            user_dic["sub_count"] = user_scores[name]["sub_count"] + 1
            if (
                user_scores[name]["correct_answers"]
                < user_dic["correct_answers"]
            ):
                user_scores[name] = user_dic
        except KeyError:
            user_dic["sub_count"] = 1
            user_scores[name] = user_dic

    out = []
    for quiz_name, user_scores in quiz_boards.items():
        out.append(html.H3(quiz_name))
        sorted_uitems = sorted(
            user_scores.items(), key=lambda e: -e[1]["correct_answers"]
        )

        rank = 1
        last_corr = None
        for idx, (uname, udic) in enumerate(sorted_uitems):
            corr = udic["correct_answers"]
            if last_corr is None:
                last_corr = corr
            if corr < last_corr:
                rank = idx + 1
            out.append(
                html.H4("{}. {} - ({})".format(rank, uname, udic["score"]))
            )
    return out
