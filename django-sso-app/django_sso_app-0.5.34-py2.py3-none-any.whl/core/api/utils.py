import json

from django.contrib.messages import get_messages
from django.utils.encoding import force_str
from django.shortcuts import reverse

from rest_framework import status

from allauth.account.adapter import get_adapter


def get_request_messages_string(request):
    """
    Serializes django messages

    :param request:
    :return:
    """
    storage = get_messages(request)
    _messages = []
    for message in storage:
        _messages.append(force_str(message))

    return ', '.join(_messages)


def get_error_response_data(response):
    """
    Extracts informations from allauth response

    :param response:
    :return:
    """
    response_data = None
    must_confirm_email = False

    if hasattr(response, 'render'):
        # rendering response
        response.render()

    response_content = getattr(response, 'content', None)
    if response_content not in [None, b'']:
        # parsing response content
        response_data = json.loads(response.content)

        response_data.pop('html')

        if response_data.get('location', None) == reverse('account_email_verification_sent'):
            must_confirm_email = True

    else:
        if response.status_code == status.HTTP_302_FOUND and response.get('location', None) == reverse('account_email_verification_sent'):
            must_confirm_email = True

    if must_confirm_email:
        response_data = get_adapter().error_messages['email_not_verified']

    return response_data
