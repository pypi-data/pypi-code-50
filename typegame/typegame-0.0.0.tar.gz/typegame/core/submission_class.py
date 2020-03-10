from dataclasses import dataclass, asdict


@dataclass()
class Submission:

    name: str
    answers: list
    correct_answers: int
    quiz_name: str

    def dict(self):
        return asdict(self)
