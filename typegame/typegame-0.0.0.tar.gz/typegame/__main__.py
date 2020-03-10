from typegame.core.app import get_app
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--port", "-p", help="define port", default=6999, type=int)
parser.add_argument("--host", "-H", help="define host", default="0.0.0.0")
parser.add_argument(
    "--quiz-path", help="directory path for quizzes", default="./quizes"
)
parser.add_argument(
    "--answer-path", help="directory path for answers", default="./answers"
)
parser.add_argument(
    "--value-game",
    help="whether to check types only or values as vell",
    action="store_true",
)

if __name__ == "__main__":
    args = parser.parse_args()
    type_only = not bool(args.value_game)
    app = get_app(
        quiz_path=args.quiz_path,
        answer_path=args.answer_path,
        type_only=type_only,
    )
    app.run_server(port=args.port, host=args.host, debug=True)
