import dash_core_components as dcc
import dash_html_components as html


quiz_body = [
    dcc.Store(id="quiz-store"),
    html.H1(children="Type Quiz"),
    html.P(
        "Try guessing what is the type of the "
        "expression in the last row of each code snippet"
    ),
    html.P(
        "There is no common state, so one variable declared "
        "in a snippet, does not affect other snippets"
    ),
    html.Div(id="question_list"),
    html.Div(id="warning-msg", style={"fontSize": "200%"}),
    html.Div(
        children=[
            html.Div(
                dcc.Input(id="name", type="text", value="Your Name Here"),
                style={"padding": 20},
            ),
            html.Div(
                html.Button(id="submit-button", n_clicks=0, children="Submit"),
                style={"padding": 20},
            ),
        ],
        id="form-submit",
    ),
    html.Div(id="output-state"),
]


def get_layout_frame(quiz_path_list):

    quiz_list = [q.split("/")[-1].split(".")[0] for q in quiz_path_list]

    quiz_options = [{"label": q.title(), "value": q} for q in quiz_list]

    return html.Div(
        children=[
            dcc.Interval(
                id="interval-component",
                interval=2 * 1000,
                n_intervals=0,  # in milliseconds
            ),
            html.Div(
                children=dcc.Dropdown(
                    options=quiz_options,
                    placeholder="Select quiz!",
                    id="quiz_list",
                ),
                style={"padding": "5px", "width": "20%"},
            ),
            html.Div(
                [
                    html.Div(
                        children=quiz_body,
                        className="nine columns",
                        style={"textAlign": "center"},
                    ),
                    html.Div(
                        children=[
                            html.H2("Leaderboard"),
                            html.Div(id="leaderboard"),
                        ],
                        className="three columns",
                    ),
                ]
            ),
        ],
        className="row",
    )
