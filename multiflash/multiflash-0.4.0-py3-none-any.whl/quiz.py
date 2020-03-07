# Copyright 2020 John Reese
# Licensed under the MIT License

import random
from functools import partial
from typing import List, Optional, Set, Type

import click

from multiflash.dataset import Fact, Facts, connect
from multiflash.question import GuessKeyword, GuessValue, Question

DEFAULT_QUESTION_TYPES = (GuessKeyword, GuessValue)


bold = partial(click.style, bold=True)


class QuizError(Exception):
    pass


class Quiz:
    def __init__(
        self,
        class_name: str,
        topic_list: Optional[List[str]] = None,
        num_choices: int = 4,
        question_limit: Optional[int] = None,
        question_types: List[Type[Question]] = None,
    ):
        self.class_name = class_name
        self.topic_list = topic_list
        self.num_choices = num_choices
        self.question_limit = question_limit
        self.question_types = question_types or DEFAULT_QUESTION_TYPES

        self.counter: int = 0
        self.questions: List[Question] = []

        self._facts: Set[Fact] = set()

    @property
    def facts(self) -> Set[Fact]:
        if not self._facts:
            db, engine = connect()
            query = Facts.select().where(Facts.class_name == self.class_name)
            if self.topic_list:
                query.where(Facts.topic.in_(self.topic_list))
            cursor = db.execute(*engine.prepare(query))
            rows = cursor.fetchall()
            self._facts.update(Fact(**row) for row in rows)
        return self._facts

    def generate(self) -> List[Question]:
        questions: List[Question] = []

        all_facts = self.facts
        if len(all_facts) < self.num_choices:
            raise QuizError("Not enough facts for meaningful quiz")
        num_incorrect = self.num_choices - 1

        for guess_type in self.question_types:
            for fact in all_facts:
                incorrect = random.sample(all_facts - {fact}, num_incorrect)
                q = guess_type(fact, incorrect)
                questions.append(q)

        random.shuffle(questions)

        if self.question_limit:
            questions = questions[: self.question_limit]

        return questions

    def ask(self, question: Question) -> bool:
        click.echo(f"\nQuestion {self.counter}: {bold(question.ask())}\n")

        letter = ord("a")
        choices = question.choices()
        answer = question.answer()

        for choice in choices:
            if question.full_answer:
                click.echo(f"  • {bold(choice)}")
            else:
                if choice == answer:
                    answer = chr(letter)
                click.echo(f"  {bold(chr(letter))}) {choice}")
                letter += 1

        response = click.prompt("\nAnswer: ", prompt_suffix="").strip()

        if response.lower() == answer.lower():
            click.secho("Correct!", fg="green")
            return True

        click.secho(f"Incorrect. Correct answer was {answer!r}", fg="red")
        return False

    def start(self):
        questions = self.generate()
        random.shuffle(questions)

        self.counter = 0
        score = 0
        for question in questions:
            self.counter += 1
            correct = self.ask(question)
            if correct:
                score += 1

        percent = (score / len(questions)) * 100
        click.secho(
            f"\nQuiz complete. You scored {score} / {len(questions)} "
            f"({percent:.0f}%) correct!",
            bold=True,
        )
