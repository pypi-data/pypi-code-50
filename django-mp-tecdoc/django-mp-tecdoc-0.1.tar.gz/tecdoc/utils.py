
from tecdoc.models import Cross


def get_crosses_text(origin, initial=None):

    if not origin:
        return

    text = initial or ''

    new_codes = Cross.objects.find(origin).codes()

    new_codes |= set(text.replace('\r', '').split('\n'))

    return '\n'.join(filter(bool, new_codes))
