# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import operator

from django.utils.deprecation import MiddlewareMixin

from .models import Notification


class NotificationMiddleware(MiddlewareMixin):
    def is_valid_request(self, request):
        return hasattr(request, 'user') and request.user.is_authenticated

    def process_request(self, request):
        """
        Adds notification status to requests for handling in views etc.
        :param request:
        :return: None
        """
        if self.is_valid_request(request):
            request.notifications = Notification.unseen(request.user)

    def process_response(self, request, response):

        if not self.is_valid_request(request):
            return response

        notifications = Notification.unseen(request.user)
        # Need to ensure cookie string is in reverse order from closest to last
        sorted_items = sorted(notifications.items(), key=operator.itemgetter(1))

        if notifications:
            epoch = datetime.datetime.utcfromtimestamp(0)
            max_age = 14 * 24 * 60 * 60
            expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age)

            coookie_string = "-".join('{}:{}'.format(
                key, (val - epoch).total_seconds() * 1000.0) for key, val in sorted_items
                                       )
            response.set_cookie(
                'notifications', coookie_string, expires=expires
            )
        else:
            response.delete_cookie('notifications')

        return response
