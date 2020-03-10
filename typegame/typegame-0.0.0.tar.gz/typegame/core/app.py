import glob
import os

import dash


from typegame.core.layout import get_layout_frame
from typegame.core.callbacks import decorate_app


EXTERNAL_STYLESHEETS = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


def get_app(
    quiz_path: str, answer_path: str, type_only: bool = True
) -> dash.Dash:

    app = dash.Dash(__name__, external_stylesheets=EXTERNAL_STYLESHEETS)
    app.config["suppress_callback_exceptions"] = True
    app.title = "Type Quiz"

    quiz_path_list = glob.glob(os.path.join(quiz_path, "*ipynb"))

    app.layout = get_layout_frame(quiz_path_list)

    os.makedirs(answer_path, exist_ok=True)

    decorate_app(app, quiz_path, answer_path, type_only)

    return app
