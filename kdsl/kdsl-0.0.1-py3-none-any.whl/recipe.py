from envparse import env  # type: ignore
from typing import Sequence, Mapping, Dict, TypeVar, Callable, Union


recipe_string: str = env.str('RECIPE')
recipe: Sequence[str] = recipe_string.split('+')


A = TypeVar('A')
def choice(**values: A) -> A:
    '''
    Use the most local value
    '''
    for r in reversed(recipe):
        try:
            return values[r]
        except KeyError:
            pass

    raise RuntimeError(
        'No choice for recipe\n'
        f'recipe: {recipe}\n'
        f'choices: {values}'
    )


def overlay(**overlays: Mapping[str, Union[A, Callable[[], A]]]) -> Mapping[str, A]:
    '''
    Use the most local values from overlays
    '''
    found: bool = False
    ret: Dict[str, A] = {}

    for r in recipe:
        values = {k: v() if callable(v) else v for k, v in overlays[r].items()}
        try:
            ret.update(values)
            found = True
        except KeyError:
            pass

    if not found:
        raise RuntimeError(
            'No overlay for recipe\n'
            f'recipe: {recipe}\n'
            f'overlays: {overlays}'
        )

    return ret
